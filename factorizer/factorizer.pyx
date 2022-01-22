import cython
from libcpp.string cimport string
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class BaseClass:

    def __init__(self, timeout=None):
        self.DETERMINISTIC = None
        self.timeout = timeout # TODO: making timeout
        pass
    
    def factorize(self, n):
        d = self._factorize(str(n).encode())
        d = int(d.decode())
        assert d*(n//d) == n
        return (d, n//d)
    
    def _factorize(self, n):
        pass

class BruteForceFactorizer(BaseClass):

    def __init__(self):
        super().__init__()
        self.DETERMINISTIC = True

    def _factorize(self, n):
        cdef:
            string d
        
        d = BruteForceFactorizer_cppfunc(n)
        return d
    
class FermatFactorizer(BaseClass):

    def __init__(self):
        super().__init__()
        self.DETERMINISTIC = True

    def _factorize(self, n):
        cdef:
            string d
        
        d = FermatFactorizer_cppfunc(n)
        return d


class PollardsRhoFactorizer(BaseClass):

    def __init__(self):
        super().__init__()
        self.DETERMINISTIC = False

    def _factorize(self, n):
        cdef:
            string d
        
        d = PollardsRhoFactorizer_cppfunc(n)
        return d