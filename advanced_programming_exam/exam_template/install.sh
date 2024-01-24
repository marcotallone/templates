#!/bin/bash

set -x

cmake -S . -B build/ || { echo "⛔ CMake failed."; exit 1; }

make -C build/ -j4 || { echo "⛔ Make failed."; exit 1; }

python3 setup.py build_ext --inplace || { echo "⛔ Python setup failed."; exit 1; }

pip install . || { echo "⛔ Pip install failed."; exit 1; }

set +x

if [ $? -eq 0 ]; then
    echo "✅ Installation successful."
else
    echo "⛔ Installation failed."
fi
