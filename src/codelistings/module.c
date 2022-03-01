#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *square(PyObject *self, PyObject *args) {
  int input;
  if (!PyArg_ParseTuple(args, "i", &input)) {
    return NULL;
  }

  return PyLong_FromLong((long)input * (long)input);
}

static PyMethodDef example_methods[] = {
    {
        "square",
        square,
        METH_VARARGS,
        "Returns a square of an integer"
    },
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef example_definition = {
    ,
    "example",
    "example module containing square() function",
    -1,
    example_methods,
};

PyMODINIT_FUNC PyInit_example(void) {
  PyObject *m = PyModule_Create(&example_definition);
  return m;
}
