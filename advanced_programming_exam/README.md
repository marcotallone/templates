# Instructions

This is just a template for my final exam of the Advanced Programming Course held at UniTs, SISSA. It is not by any means the only/the correct way to organize the second part of this exam but it is what I did and what I would suggest others to do to keep all the code organized and to make overall compilation easier. This will not automatically guarantee to pass the exam of course but it will give you more time to focus on the code itself rather than on compilation errors and documentation writing...

In order to use this template you should follow the instructions below:

* copy the `exam_template` folder in this repository on your machine and change its name according to what the professor asks.

* implement your header file(s) in the `include/` folder (name of the header can be changed)

* implement your source code and your pybindings in the `src/` folder (name of the files can be changed)

* implement your main or other scripts in the `apps/` folder
  
* to compile you should modify ONLY the `CMakeLIsts.txt` files in the `apps/` and `src/` folders. Parts that need to be changed have been highlighted in the relative scripts.

* To compile the pybindings with setuptools, change the names of the files and the name of the module where it has been highlighted in the `setup.py`

* follow compilations instructions (or use the `install.sh`) below in the pre-written README to compile.

To conclude also remember to update the README with the following:

* change the names of your files/headers/libraries/modules in the pre-written documentation (README)

* change your name and relative info

* change the exam date above and the year (if needed)

* complete the "Implemented Features" part with the description of what you did + add eventual dependencies

> [!WARNING]
> 🚨 **WARNINGS**:
>
> * **DO NOT CHANGE** THE NAMES OF THE FOLDERS or THE POSITIONS OF THE FILES: that might lead to errors and it might require to rewrite the cmake...
> * ⚠️⚠️⚠️ **DO NOT COPY THIS README IN THE EXAM FOLDER!** ⚠️⚠️⚠️
> * This set-up has been tested and I've used it myself successfully, but I suggest you test it before the exam so you can get familiar using it. Right now this template only works for exams in which a cmake+pybinding set-up is required and it's only able to compile the C++ code into a shared library (small modifications are required for a static one). You're more than welcome to signal any problem by opening an issue in this repository.

Good Luck 🍀
