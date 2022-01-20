from distutils.core import setup, Extension
from tabnanny import verbose
from Cython.Build import cythonize
import glob
import setuptools


### Compile with Cython begins ###
ext = Extension("factorizer", 
    sources = glob.glob("factorizer/*.pyx")+glob.glob("factorizer/*.Factorizer_cpp"),
    include_dirs = ['./factorizer'],
    language = "c++",
    extra_compile_args = ["-v", "-std=c++11"],
    extra_link_args = ["-std=c++11"]
)
setup(
    name = "factorizer", 
    ext_modules = cythonize([ext],language_level=3)
)

### Compile with Cython ends ###



### For downlode through GitHub begins ###
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "factorizer",
    version = "0.0.1",
    author = "Fulltea",
    author_email = "rikuta@furutan.com",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/FullteaOfEEIC/factorizer",
    packages=setuptools.find_packages(),
    python_requires='>=3'
)


### For downlode through GitHub ends ###