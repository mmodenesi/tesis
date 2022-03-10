/* Inclusión de las librearías de Python,
 * para usar PyObject, PyArg_ParseTuple, etc... **/
#define PY_SSIZE_T_CLEAN
#include <Python.h>

/* Definimos la función que computa el cuadrado de un entero */
static PyObject *square(PyObject *self, PyObject *args) {
  int input;
  if (!PyArg_ParseTuple(args, "i", &input)) {
    return NULL;
  }

  return PyLong_FromLong((long)input * (long)input);
}

/* Debemos incluir el nombre y la dirección de la función
 * en una tabla de métodos */
static PyMethodDef ExampleMethods[] = {
    {
        "square",
        square,
        METH_VARARGS,
        "Returns a square of an integer"
    },
/* Valor "sentinela", señala el final del arreglo */
    {NULL, NULL, 0, NULL},
};


/* Definición del módulo, para que podamos
 * importarlo desde el intérprete de Python */
static struct PyModuleDef examplemodule = {
    PyModuleDef_HEAD_INIT,
    "example",
    "example module containing square() function",
    -1,
    ExampleMethods,
};

/* Esta función será llamada cuando se inizialice el módulo
 * en el intérprete de Python */
PyMODINIT_FUNC PyInit_example(void) {
  PyObject *m = PyModule_Create(&examplemodule);
  return m;
}
