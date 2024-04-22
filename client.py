#client.py



import socket

def query_word(word):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("localhost", 9999))
        client_socket.send(("QUERY:" + word).encode())
        meaning = client_socket.recv(1024).decode().split(":")[1]
        print("Meaning:", meaning)

if __name__ == "__main__":
    word = input("Enter word to search: ")
    query_word(word)
