import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5001))
print("Enter quit to exit.")

while True:
    message = input("You: ")

    if message.lower() == "quit":
        break

    client.send(message.encode())

client.close()