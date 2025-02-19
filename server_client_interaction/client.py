import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))

    message = client_socket.recv(256).decode("utf-8")
    print(message)

    first_number = input("Enter your guess: ")
    client_socket.send(first_number.encode("utf-8"))

    result = client_socket.recv(256).decode("utf-8")
    print(result)

    client_socket.close()

if __name__ == "__main__":
    start_client()