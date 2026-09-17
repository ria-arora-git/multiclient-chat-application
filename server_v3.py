import socket
import threading

clients=[]

def broadcast(message,sender):
    for c in clients:
        if c!=sender:
            c.send(message)

def handle_client(client, address):
    print("Connected:", address)

    clients.append(client)

    while True:
        message = client.recv(1024)

        if not message: \
            break

        print(address, "said:", message.decode())

        broadcast(message,client)

    clients.remove(client)
    client.close()
    print("Disconnected:", address)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5001))
server.listen()

print("Server is running...")

while True: 
    client, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()