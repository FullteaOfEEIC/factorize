from distutils.core import setup, Extension
from tabnanny import verbose
from Cython.Build import cythonize
import glob

ext = Extension("factorizer", 
    sources=glob.glob("factorizer/*.pyx")+glob.glob("factorizer/*.Factorizer_cpp"),
    include_dirs=['./factorizer'],
    language="c++",
    extra_compile_args=["-v", "-std=c++11"],
    extra_link_args=["-std=c++11"]
)
setup(name="factorizer", ext_modules=cythonize([ext],language_level=3))