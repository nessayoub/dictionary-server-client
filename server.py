#server.py

import socket
from concurrent.futures import ThreadPoolExecutor

def handle_client(client_socket, address, dictionary):
    data = client_socket.recv(1024).decode()
    word = data.split(":")[1]
    meaning = dictionary.get(word, "Word not found")
    client_socket.send(("MEANING:" + meaning).encode())
    client_socket.close()

def start_server(host, port, dictionary):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print("Server listening on", (host, port))
        with ThreadPoolExecutor(max_workers=5) as executor:
            while True:
                client_socket, address = server_socket.accept()
                executor.submit(handle_client, client_socket, address, dictionary)

if __name__ == "__main__":
    # Load dictionary data from file or define here
    dictionary = {"apple": "A fruit", "banana": "Another fruit", "Ayoub" : "A name", "Distributed Systems" : "University course"}

    start_server("localhost", 9999, dictionary)
