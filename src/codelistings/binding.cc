#include <pybind11/pybind11.h>
#include "omnetpp/csimplemodule.h"
#include "omnetpp/cmessage.h"

using namespace omnetpp;
namespace py = pybind11;

/* una clase que hereda de cSimpleModule (OMNeT++)
 * para exponer algunos métodos virtuales */
class cSimpleModulePublicist : public cSimpleModule {
public:
    using cSimpleModule::handleMessage;
    using cSimpleModule::initialize;
    using cSimpleModule::send;
    using cSimpleModule::getName;
};

/* la clase que va a ver el intŕeprete de Python */
class PycSimpleModule : public cSimpleModule {
public:
    using cSimpleModule::cSimpleModule;

    void initialize() override {
        PYBIND11_OVERLOAD(void, cSimpleModule, initialize, );
    }

    void handleMessage(cMessage *msg) override {
        PYBIND11_OVERLOAD(void, cSimpleModule, handleMessage, msg);
    }
    ~PycSimpleModule() {}
};

/* definición del módulo */
PYBIND11_MODULE(pyopp, m) {

    m.doc() = "The Python binding for OMNeT++";

    // cMessage
    py::class_<cMessage> py_cMessage(m, "cMessage");
    py_cMessage.def(
        py::init<const char*, short>(),
        py::arg("name") = nullptr, y::arg("kind") = 0);

    // cSimpleModule
    py::class_<
        cSimpleModule,
        PycSimpleModule> py_cSimpleModule(m, "cSimpleModule");
    py_cSimpleModule.def(
        py::init<unsigned>(),
        py::arg("stacksize") = 0);
    py_cSimpleModule.def(
        "handleMessage", 
         &cSimpleModulePublicist::handleMessage);
    py_cSimpleModule.def(
        "initialize",
        (void (cSimpleModule::*)()) &cSimpleModulePublicist::initialize);
    py_cSimpleModule.def(
    "getName", &cSimpleModulePublicist::getName);
    py_cSimpleModule.def(
        "send",
        py::overload_cast<cMessage*,
                          const char*,
                          int>(&cSimpleModule::send),
        py::arg("msg"), py::arg("gatename"), py::arg("gateindex") = -1);
}
