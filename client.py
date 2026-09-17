import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",5001))

client.send("Hello from client.".encode())

message = client.recv(1024)
print("Server said : ", message.decode())

client.close()