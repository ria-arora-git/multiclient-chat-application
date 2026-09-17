import socket
import threading

def handle_client(client, address):
    print("Connected:", address)

    while True:
        message = client.recv(1024)

        if not message:  # If we didn't receive any data, assume the client disconnected
            break

        print(address, "said:", message.decode())

    client.close()
    print("Disconnected:", address)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5001))
server.listen()

print("Server is running...")

while True:  # continuously accepts new clients.
    client, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()