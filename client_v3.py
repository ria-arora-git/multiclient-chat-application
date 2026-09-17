import socket
import threading

def receive_messages():
    while True:
        message = client.recv(1024)
        if not message:
            break

        print("\nMessage:", message.decode())


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5001))

thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    message = input("You: ")

    if message.lower() == "quit":
        break

    client.send(message.encode())

client.close()