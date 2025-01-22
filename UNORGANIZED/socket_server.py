"""This file demonstrates a simple socket server that asks certain questions to the client."""
import socket


def start_server():
    host = '127.0.0.1'  # localhost
    port = 65432        # Port to listen on

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server started and listening on {host}:{port}")

    while True:
        # Accept a connection
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        # Handle the connection
        with conn:
            conn.sendall("Welcome! Please enter your name: ".encode('utf-8'))
            name = conn.recv(1024).decode('utf-8')
            print(f"Client's name: {name}")

            conn.sendall(f"Hi {name}, please tell me your phone number: ".encode('utf-8'))
            phone_number = conn.recv(1024).decode('utf-8')
            print(f"Client's phone number: {phone_number}")

            conn.sendall("Please describe your complaint: ".encode('utf-8'))
            complaint = conn.recv(1024).decode('utf-8')
            print(f"Client's complaint: {complaint}")

            conn.sendall("I registered your complaints. Ending the conversation.".encode('utf-8'))
            print("Conversation ended. Closing client connection.")
            conn.close()  # Close the client connection explicitly


if __name__ == "__main__":
    start_server()
