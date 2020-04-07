import socket



def start_server_program():
    host = socket.gethostname()
    port = 8888
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    print("Waiting for a connection, host: " + host + ", port: " + str(port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("connection From: " + str(address))
    return conn, address


if __name__ == "__main__":
    conn, address = start_server_program()
    try:
        while True:
            data = conn.recv(4096).decode()
            if data:
                print("From connected user: " + str(data))
    except KeyboardInterrupt:
        pass
    finally:
        conn.close()
        print("Ending Program, closing connection")