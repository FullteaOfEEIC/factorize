import cython
from libcpp.string cimport string
import signal
from Errors import *
signal.signal(signal.SIGINT, signal.SIG_DFL)

class BaseClass:

    def __init__(self):
        pass
    
    def factorize(self, n):
        d = self._factorize(str(n).encode())
        d = int(d.decode())
        assert d*(n//d) == n
        return (d, n//d)
    
    def _factorize(self, n):
        pass

class BruteForceFactorizer(BaseClass):

    def _factorize(self, n):
        cdef:
            string d
        
        d = BruteForceFactorizer_cppfunc(n)
        return d
    
class FermatFactorizer(BaseClass):

    def _factorize(self, n):
        cdef:
            string d
        
        d = FermatFactorizer_cppfunc(n)
        return d