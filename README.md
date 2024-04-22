# dictionary-server-client


# Multi-threaded Dictionary Server

This project implements a multi-threaded dictionary server in Python. The server allows clients to connect and query the meaning of words from a predefined dictionary. Additionally, the project includes both command-line and graphical user interface (GUI) clients for interacting with the server.

## Overview

The dictionary server follows a client-server architecture, with the server capable of handling multiple client connections concurrently using a multi-threaded approach. It listens for incoming connections and responds to word queries by looking up definitions from a predefined dictionary.

## Components

### Server

The `server.py` script implements the multi-threaded dictionary server. It listens for incoming connections from clients and handles word queries by looking up definitions from a predefined dictionary.

### Command-Line Client

The `client.py` script provides a command-line interface for querying word meanings. It connects to the server and sends word queries, displaying the responses received from the server.

### GUI Client

The `gui_client.py` script offers a graphical user interface (GUI) for interacting with the dictionary server. It allows users to enter words in an entry field and click a button to query meanings, with the results displayed in a message box.

## Usage

1. **Server**:

   - Navigate to the directory containing `server.py`.
   - Run the server script: `python server.py`

2. **Command-Line Client**:

   - Navigate to the directory containing `client.py`.
   - Run the client script: `python client.py`

3. **GUI Client**:
   - Navigate to the directory containing `gui_client.py`.
   - Run the GUI client script: `python gui_client.py`

## Requirements

- Python 3.x
- tkinter

## Acknowledgements

The project was developed as part of a learning exercise and may contain code snippets or concepts inspired by various educational resources and tutorials.
