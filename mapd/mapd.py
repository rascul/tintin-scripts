from twisted.protocols import basic

class Mapd(basic.LineReceiver):
	def connectionMade(self):
		self.factory.clients.append(self)

	def connectionLost(self, reason):
		self.factory.clients.remove(self)

	def lineReceived(self, line):
		for c in self.factory.clients:
			c.message(line)

	def message(self, message):
		self.transport.write(message + '\n')

from twisted.internet import protocol
from twisted.application import service, internet

factory = protocol.ServerFactory()
factory.protocol = Mapd
factory.clients = []

application = service.Application("mapd")
internet.TCPServer(2222, factory).setServiceParent(application)
