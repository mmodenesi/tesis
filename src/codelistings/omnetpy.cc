#include <omnetpp/omnetpy.h>
#include <pybind11/pybind11.h>

static omnetpp::cObject *F1() {
    auto py_module = pybind11::module::import("txc");
    pybind11::object obj = py_module.attr("PyTxc")();
    obj.inc_ref();
    return obj.cast<omnetpp::cObject *>();
}

static void *F2(omnetpp::cObject *obj) {
    return (void*)dynamic_cast<PycSimpleModule*>(obj);
}

void F3() {
    InterpreterManager::ensureInterpreter();
    omnetpp::classes.getInstance()->add(
    new omnetpp::cObjectFactory("PyTxc", F1, F2, "module"));
}

static omnetpp::CodeFragments cf(F3, omnetpp::CodeFragments::STARTUP);
