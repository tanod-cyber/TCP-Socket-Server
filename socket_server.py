import socket
import time

#Title
name = "tcp socket server"
title = name.title()
print(title)


#TYPE THE IP HERE
ip = str(input("Type The Ip Here: ")).strip()

if ip == "":
  ip = "0.0.0.0"

#TO CREATE TCP SOCKET
print("Creating TCP SOCKET....")
time.sleep(3)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#TO LISTEN THE IP + PORTS
server.bind((ip, 5000))
print(f"Connecting {ip} port 5000")

#LISTENING
server.listen(1)
print("listening please wait.....")

#ACCEPTING
client_socket, addr = server.accept()
print("Connected:", addr)

#RECEIVE THE DATA AND DECODE IT
#WITH LOOP TO CAPTURE ALL DATA
while True:
  try:
    data = client_socket.recv(1024)
      #IF NOT DATA THEN STOP
    if not data:
      print("Out of data")
      break
    #LETS DECODE IT
    print("Receive data:", data.decode(errors="ignore"))
    
    #send some message here
    client_socket.send(b"Hi there!")
  
  except Exception as e:
    print("Error", e)
    break
      

#CLIENT AND SERVER CLOSE
close = "server and client are now closing"
closing = close.title()
print(closing)

client_socket.close()
server.close()
