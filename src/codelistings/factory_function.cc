static omnetpp::cObject *F1()  // factory function
{
    // importamos el módulo donde está definida la clase
    auto py_module = py::module::import("txc1");

    // Instanciamos la clase, obteniendo un py::object
    py::object obj = py_module.attr("PyTxc1")();
    
    // conversión a cSimpleModule (la clase base)
    cSimpleModule *tmp = obj.cast<cSimpleModule *>();
    
    // conversión a la clase base de cSimpleModule
    cObject *ret = dynamic_cast<cObject*>(tmp);
    return ret;
}
