static omnetpp::cObject *__factoryfunc_13()
{
    omnetpp::cModule *ret = new Txc1;
    return ret;
}

static void *__castfunc_13(omnetpp::cObject *obj)
{
    return (void*)dynamic_cast<Txc1*>(obj);
}

namespace
{
    void __onstartup_func_13()
    {
        omnetpp::classes.getInstance()->add(
            new omnetpp::cObjectFactory(
                omnetpp::opp_typename(typeid(Txc1)),
                __factoryfunc_13,
                __castfunc_13,
                "module"));
    }

    static omnetpp::CodeFragments __onstartup_obj_13(
        __onstartup_func_13,
        omnetpp::CodeFragments::STARTUP);
}
