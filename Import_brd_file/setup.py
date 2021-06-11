from distutils.core import setup
from Cython.Build import cythonize

setup(name='Initial HFSS',
     ext_modules=cythonize('initial.py'))