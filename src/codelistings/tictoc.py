from pyopp import cSimpleModule, cMessage


class PyTxc(cSimpleModule):
    def initialize(self):
        if self.getName() == 'tic':
            self.send(cMessage('msg'), 'out')
    
    def handleMessage(self, msg):
        self.send(msg, 'out')
