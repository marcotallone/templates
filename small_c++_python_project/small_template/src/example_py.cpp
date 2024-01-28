#include ""

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>

namespace py = pybind11;
using namespace pybind11::literals;

PYBIND11_MODULE(example_py, m)
{
    m.doc() = "Example module for pybind11";

}
