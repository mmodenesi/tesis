simple PyTxc
{
    gates:
        input in;
        output out;
}
    
//
// Two instances (tic and toc) of Txc1 connected both ways.
// Tic and toc will pass messages to one another.
//
network PyTictoc
{
    submodules:
        tic: PyTxc;
        toc: PyTxc;
    connections:
        tic.out --> {  delay = 100ms; } --> toc.in;
        tic.in <-- {  delay = 100ms; } <-- toc.out;
}
