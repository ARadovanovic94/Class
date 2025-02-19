import socket
import random

def handle_client(client_socket):
    secret_number = random.randint(1, 10)

    client_socket.send("Enter a number between 1 and 10: ".encode("utf-8"))
    first_number = int(client_socket.recv(256).decode("utf-8"))

    if first_number == secret_number:
        result = "Congratulations! You guessed the number."
    else:
        result = f"Unfortunately, you did not guess the number. The correct number was {secret_number}."

    client_socket.send(result.encode("utf-8"))
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen()

    print("Server is listening on port 12345...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()