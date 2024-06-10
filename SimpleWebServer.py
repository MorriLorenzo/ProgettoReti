#!/bin/env python
#Autore: Lorenzo Morri 
#Matricola:0001077662
import http.server
import socketserver
import threading

#Num porta
port = 8080

# Uso il ThreadingTCPServer per gestire piu' richieste
server = socketserver.ThreadingTCPServer(('',port), http.server.SimpleHTTPRequestHandler )

#Termina correttamente tutti i thread
server.daemon_threads = True  
#Sovrascrivo per riutilizzare socket  
server.allow_reuse_address = True  

#Funzione che termina processo
def stop_server():
  input("Press Enter to stop the server...")
  #Ferma serve_forever()
  server.shutdown()

# Riceve input tastiera
input_thread = threading.Thread(target=stop_server)
input_thread.daemon = True
input_thread.start()

try:
  print("Serving at port", port)
  server.serve_forever()
except KeyboardInterrupt:
  pass
finally:
  #Eccezioni o meno chiude tutto
  server.server_close()