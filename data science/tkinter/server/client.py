from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ClientFactory as clif
from twisted.internet.endpoints import TCP4ClientEndpoint

class client(Protocol):
    def _init_ (self):
        reactor.callInThread(self.send_data)
    def dataReceived(self, data):
        data=data.decode('utf-8')
        print(data)
    def sent_data(self):
        while True:
           self.transport.write(input(":::").encode('utf-8'))
    


class clientFactory(clif):
    def buildProtocol(self, addr):
        return client()


if __name__=='_main_':
    endpoint=TCP4ClientEndpoint(reactor,"host4",3000)
    endpoint.connect(clif)
    reactor.run()