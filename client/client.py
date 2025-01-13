import socket
import os
import sys

# Configuration via environment variables
SERVER_HOST = os.getenv("SERVER_HOST", "127.0.0.1")  # Default to localhost
SERVER_PORT = int(os.getenv("SERVER_PORT", 5000))  # Default port 5000


def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            print(f"Connecting to server at {SERVER_HOST}:{SERVER_PORT}...")
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            print("Connected to server!")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    print("Connection closed by server")
                    break
                print(f"Received: {data.decode('utf-8').strip()}")
        except KeyboardInterrupt:
            print("\nClient is shutting down gracefully...")
            sys.exit(0)  # Gracefully exit on Ctrl + C
        except Exception as e:
            print(f"Error occurred: {e}")
            sys.exit(1)


if __name__ == "__main__":
    run_client()
