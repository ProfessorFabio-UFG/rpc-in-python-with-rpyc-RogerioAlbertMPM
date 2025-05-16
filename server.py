import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value
  
  def exposed_uppercase(self, text):
    return text.upper()
  
  def exposed_lowercase(self, text):
    return text.lower()
  
  def exposed_reverse(self, text):
    return text[::-1]

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

