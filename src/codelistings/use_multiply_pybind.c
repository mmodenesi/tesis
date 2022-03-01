#include <iostream>
#include <pybind11/embed.h>

namespace py = pybind11;

int main() {
    // start interpreter and keep it alive
    py::scoped_interpreter guard{};

    // import mul.py
    py::module m = py::module::import("mul");

    // call function multiply
    py::object result = m.attr("multiply")(12, 3);

    std::cout << "Result is " << result.cast<int>() << std::endl;
    return 0;
}
