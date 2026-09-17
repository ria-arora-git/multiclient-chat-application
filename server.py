import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.01",5001))
server.listen()

print("Server is waiting for connection...")

client, address = server.accept()
print("client connected : ", address)

message = client.recv(1024)

print("Client said : ", message.decode())

client.send("hello from server".encode())

client.close()
server.close()
