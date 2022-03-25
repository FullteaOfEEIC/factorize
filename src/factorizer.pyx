from libcpp.string cimport string
import requests
from requests.exceptions import Timeout as requestsTimeoutError
import threading
import time


class TimeOutError(Exception):
    pass



class BaseClass:

    def __init__(self, timeout=None):
        if timeout is None or timeout<0:
            self.timeout = None
        else:
            self.timeout = timeout

        self.result = {}
        
    def factorize(self, n, *args, **kwargs):
        assert n>=0
        if n==0:
            return (0, 0)
        elif n==1:
            return (1, 1)
        elif n%2==0: # some algorithms can't get correct answer for 2(this is a prime) or even numbers.
            return (2, n//2)
        args = (str(n).encode(),)+args
        thread_factorize = threading.Thread(target=self.factorize_wrap, args=args, kwargs=kwargs, name="_factorize", daemon=True)
        thread_factorize.start()
        if self.timeout is not None:
            for i in range(self.timeout*100):
                if thread_factorize.is_alive() == False:
                    break
                time.sleep(0.01)
            else:
                raise TimeOutError
        else:
            thread_factorize.join()


        d = self.result[str(n).encode()]
        d = int(d.decode())
        assert d*(n//d) == n
        return (d, n//d)

    
    def factorize_wrap(self, n, *args, **kwargs):
        d = self._factorize(n, *args, **kwargs)
        self.result[n] = d

    
    def _factorize(self, string n, *args, **kwargs):
        return b"1"


class BruteForceFactorizer(BaseClass):

    def __init__(self, timeout=None):
        super().__init__(timeout)

    def _factorize(self, string n, *args, **kwargs):
        cdef:
            string d
        with nogil:
            d = BruteForceFactorizer_cppfunc(n)
        return d


class FermatFactorizer(BaseClass):

    def __init__(self, timeout=None):
        super().__init__(timeout)

    def _factorize(self, string n, *args, **kwargs):
        cdef:
            string d
        with nogil:
            d = FermatFactorizer_cppfunc(n)
        return d


class PollardsRhoFactorizer(BaseClass):

    def __init__(self, c=1, timeout=None):
        super().__init__(timeout)
        self.c = c

    def _factorize(self, string n, *args, **kwargs):
        cdef:
            string d
            long c
        c = self.c
        with nogil:
            d = PollardsRhoFactorizer_cppfunc(n, c)
        return d


class PminusOneFactorizer(BaseClass):

    def __init__(self, step=1, timeout=None):
        assert int(step) in (1,2)
        super().__init__(timeout)
        self.step = int(step)
    
    def factorize(self, n, M=100000, *args, **kwargs):
        assert M<ULONG_MAX
        return super().factorize(n, M, *args, **kwargs)
    
    def _factorize(self, string n, unsigned long M, *args, **kwargs):
        cdef:
            string d
        if self.step==1:
            while True:
                with nogil:
                    d = PminusOneFactorizer_step1_cppfunc(n, M)
                if d!=n:
                    return d
                else:
                    M = M//2

        else:
            with nogil:
                d = PminusOneFactorizer_step2_cppfunc(n, M)
        return d

class RSAPrivateKeyFactorizer(BaseClass):

    def __init__(self, timeout=None):
        super().__init__(timeout)

    def factorize(self, n, d, e=65537, *args, **kwargs):
        return super().factorize(n, str(d).encode(), str(e).encode(), *args, **kwargs)

    def _factorize(self, string n, string d, string e, *args, **kwargs):
        cdef:
            string p
        with nogil:
            p = RSAPrivateKeyFactorizer_cppfunc(n, d, e)
        return p



class FactorDBFactorizer(BaseClass):
    
    def __init__(self, timeout=None):
        super().__init__(timeout)
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
            return (1, n)
        else:
            d = int(result[0][0])
            assert d*(n//d) == n
            return (d, n//d)