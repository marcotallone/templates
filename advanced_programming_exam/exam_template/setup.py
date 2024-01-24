from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys
import setuptools

# Helper class to determine the pybind11 include path.
class get_pybind_include(object):
    def __str__(self):
        import pybind11
        return pybind11.get_include()

ext_modules = [
    Extension(
        'python_module_name',                                      # <--- CHANGE WITH YOUR MODULE NAME
        ['src/source_py.cpp','src/soure1.cpp','src/source2.cpp'],  # <--- CHANGE WITH YOUR SOURCE FILES IN THE src/ FOLDER
        include_dirs=[
            get_pybind_include(),
            # '/path/to/other/includes',                           # <--- ADD ADDITIONAL PATHS IF NEEDED
        ],
        language='c++'
    ),
]

setup(
    name='python_module_name',                                   # <--- CHANGE WITH YOUR MODULE NAME
    version='1.0',                                               # <--- CHANGE WITH YOUR VERSION
    author='Name Surname',                                       # <--- CHANGE WITH YOUR NAME
    author_email='name_surname@mail.com',                        # <--- CHANGE WITH YOUR EMAIL 
    description='Advanced Programming Exam',
    long_description='',
    ext_modules=ext_modules,
    install_requires=['pybind11>=2.5.0'],  # pybind11 requirement.
    cmdclass={'build_ext': build_ext},
    zip_safe=False,
)
