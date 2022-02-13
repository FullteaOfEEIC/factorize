from setuptools import setup, Extension, find_packages
import os
import glob

sources = [] 
sources += glob.glob("src/*.cpp")
sources += glob.glob("src/*.pyx")
    
ext = Extension("factorizer", 
    sources = sources,
    language = "c++",
    extra_compile_args = ["-v", "-std=c++14", "-Wall", "-O3"],
    extra_link_args = ["-std=c++14"]
)

with open("README.md", "r") as fp:
    long_description = fp.read()
with open("requirements.txt", "r") as fp:
    install_requires = fp.read().splitlines()

setup(
    name = "factorizer",
    version = "0.5.2",
    author = "Fulltea",
    author_email = "rikuta@furutan.com",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/FullteaOfEEIC/factorizer",
    packages = find_packages(where="src"),
    package_dir = {
        "factorizer": "src"
    },
    install_requires = install_requires,
    ext_modules = [ext]
)

if os.path.exists(os.path.join("src", "factorizer.cpp")):
    os.remove(os.path.join("src", "factorizer.cpp"))
