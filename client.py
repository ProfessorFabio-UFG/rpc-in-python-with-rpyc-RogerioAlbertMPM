import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  conn.root.exposed_append(5)       # Call an exposed operation,
  conn.root.exposed_append(6)       # and append two elements
  print (conn.root.exposed_value())   # Print the result

  txt = "Python RPC DistSys"
  print("uppercase: ", conn.root.exposed_uppercase(txt))
  print("lowercase: ", conn.root.exposed_lowercase(txt))
  print("reverse: ", conn.root.exposed_reverse(txt))

  conn.close()