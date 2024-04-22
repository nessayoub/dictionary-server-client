#gui_client.py


import socket
import tkinter as tk
from tkinter import messagebox

def query_word():
    word = entry_word.get()
    if not word:
        messagebox.showerror("Error", "Please enter a word.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect(("localhost", 9999))
            client_socket.send(("QUERY:" + word).encode())
            meaning = client_socket.recv(1024).decode().split(":")[1]
            messagebox.showinfo("Meaning", meaning)
        except ConnectionRefusedError:
            messagebox.showerror("Error", "Connection refused. Please make sure the server is running.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Dictionary Client")

label_word = tk.Label(root, text="Enter word:")
label_word.grid(row=0, column=0, padx=10, pady=10)

entry_word = tk.Entry(root)
entry_word.grid(row=0, column=1, padx=10, pady=10)

button_search = tk.Button(root, text="Search", command=query_word)
button_search.grid(row=1, columnspan=2, padx=10, pady=10)

root.mainloop()
