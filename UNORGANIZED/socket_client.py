"""This file demonstrates a simple socket client that communicates with a server."""
import socket


def start_client():
    host = '127.0.0.1'  # Server address
    port = 65432        # Server port

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(data)
            message = input("Your response: ")
            client_socket.sendall(message.encode('utf-8'))

            # If the server ends the conversation, close the connection
            if "Ending the conversation." in data:
                print("Server ended the conversation. Closing connection.")
                break
    finally:
        # Close the client socket
        client_socket.close()
        print("Disconnected from server.")


if __name__ == "__main__":
    start_client()
