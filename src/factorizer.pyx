from libcpp.string cimport string
import requests
from requests.exceptions import Timeout as requestsTimeoutError
import threading
import time
from multiprocessing import cpu_count, Process
from cython.parallel import prange
import ctypes
cimport openmp

class TimeOutError(Exception):
    pass

"""
class Thread_With_Stop(threading.Thread):

    def __init__(self, target, n, name, *args, **kwargs):
        args = (n,)+args
        super().__init__(target=target, name=name, args=args, kwargs=kwargs)
        self._stop_event = threading.Event()
    
    def stop(self):
        self._stop_event.set()

    def is_stopped(self):
        return self._stop_event.is_set()
"""


class BaseClass:

    def __init__(self, timeout=None, n_jobs=1):
        if timeout is None or timeout<0:
            self.timeout = None
        else:
            self.timeout = timeout
        
        if n_jobs == -1:
            self.n_jobs = cpu_count()
        elif n_jobs is None:
            self.n_jobs = 1
        else:
            self.n_jobs = n_jobs

        self.result = {}

    def factorize(self, n, *args, **kwargs):
        assert n>=0
        if n==0:
            return (0, 0)
        elif n==1:
            return (1, 1)
        args = (str(n).encode(),)+args
        thread_factorize = threading.Thread(target=self.factorize_wrap, name="_factorize", daemon=True, args=args, kwargs=kwargs)
        thread_factorize.start()
        thread_factorize.join(timeout=self.timeout)
        if thread_factorize.is_alive():
            raise TimeOutError
        assert thread_factorize.is_alive() == False
        d = self.result[str(n).encode()]
        d = int(d.decode())
        assert d*(n//d) == n
        return (d, n//d)

    
    def factorize_wrap(self, n, *args, **kwargs):
        d = self._factorize(n=n, args=args, kwargs=kwargs["kwargs"])
        self.result[n] = d

    
    def _factorize(self, string n, *args, **kwargs):
        return b"1"


class BruteForceFactorizer(BaseClass):

    def _factorize(self, string n, *args, **kwargs):
        cdef:
            string d
            long n_jobs
        n_jobs = self.n_jobs
        with nogil:
            d = BruteForceFactorizer_cppfunc(n, n_jobs)
        return d


class FermatFactorizer(BaseClass):

    def _factorize(self, string n, *args, **kwargs):
        cdef:
            string d
        with nogil:
            d = FermatFactorizer_cppfunc(n)
        return d


class PollardsRhoFactorizer(BaseClass):

    def __init__(self, c=1, timeout=None, n_jobs=1):
        super().__init__(timeout=timeout, n_jobs=n_jobs)
        self.c = c


    def _factorize(self, string n, *args, **kwargs):
        cdef:
            string d
            long c
            long n_jobs
        c = self.c
        with nogil:
            d = PollardsRhoFactorizer_cppfunc(n, c)
        return d


class RSAPrivateKeyFactorizer(BaseClass):

    def factorize(self, n, d, e=65537, *args, **kwargs):
        kwargs["d"] = d
        kwargs["e"] = e
        return super().factorize(n=n, args=args, kwargs=kwargs)


    def _factorize(self, string n, *args, **kwargs):
        cdef:
            string p, d, e
        d = str(kwargs["kwargs"]["d"]).encode()
        e = str(kwargs["kwargs"]["e"]).encode()
        with nogil:
            p = RSAPrivateKeyFactorizer_cppfunc(n, d, e)
        return p


class FactorDBFactorizer(BaseClass):
    
    def __init__(self, timeout=None, n_jobs=1):
        super().__init__(timeout=timeout, n_jobs=n_jobs)
        self.ENDPOINT = "http://factordb.com/api"

    
    def _factorize(self, n):
        payload = {"query": n}
        try:
            r = requests.get(self.ENDPOINT, params=payload, timeout=self.timeout)
            return r.json()
        except requestsTimeoutError:
            raise TimeOutError
        except Exception as e:
            raise e


    def factorize(self, n, raw_result=False):
        if n==0:
            return (0, 0)
        elif n==1:
            return (1, 1)
        result = self._factorize(n)["factors"]
        if raw_result:
            return result
        
        if len(result)==1 and result[0][1]==1:
            return (1,n)
        else:
            d = int(result[0][0])
            assert d*(n//d) == n
            return (d, n//d)


