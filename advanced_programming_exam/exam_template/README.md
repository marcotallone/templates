# Advanced Programming Exam

### SISSA, UniTs, 2023 - 2024

### 17 Jan 2024

***

## Documentation

## Student's Info

| Name | Surname | Student ID | UniTs mail | Classroom mail | Master |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Your_Name | Your_Surname | ID00000000 | name.surname@studenti.units.it | namesurname@mail.com | SDIC (only correct choice 😎) |

## Project's organization

The project is organized with the following structure:

```bash
.
├── apps # Ready-to-use scripts
│   ├── main.cpp
│   └── main.py
├── include # Include headers
│   └── header.hpp
├── README.md
├── setup.py # Setuptools installation
├── install.sh # Quick compilation and installation
└── src # Source files and pybindings
    ├── source.cpp
    └── bindings_py.cpp
```

## Usage

To be able to use the implemented library in a `C++` script it's possible to import the `header_name.hpp` header file and link to the library at compilation time. Compilation details are explained below.

```cpp
#include "header_name.hpp"
```

For `Python` scripts the import of the `module_name` module it's necessary to use the implemented features. Further details on how to install the dedicated modules are explained below.

```python
import module_name
```

## Implemented Features

## Dependencies

The following libraries are required for the project to be compiled:

* [PyBind11](https://pybind11.readthedocs.io/en/stable/) - version 2.11.1 ([licence](https://github.com/pybind/pybind11/blob/master/LICENSE))

## Compilation

Compilation of the implemented library is performed with the `cmake` system.\
By executing the following commands (and aventually specifying the correct `-DCCMAKE_PREFIX_PATH` for eventual third party libraries if not found) all the `C++` libraries, as well as the python pybind11 modules, will be compiled in the `build/` folder.

```bash
cmake -S . -B build/

make -C build/ -j<N>
```

To be able to import the implemented python modules, a `setup.py` script has been implemented to make installation easier.\
Installing the python module is possible by running the following commands from the root folder of the project:

```bash
python setup.py build_ext --inplace

pip install .
```

For a quick installation following this commands and `install.sh` script has been provided in the root folder.
