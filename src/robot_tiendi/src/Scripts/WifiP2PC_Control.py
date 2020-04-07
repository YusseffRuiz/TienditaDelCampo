import socket
import subprocess


def cmd_p2p_pi(cmd):
    command = "p2p_" + cmd
    p = subprocess.Popen(["wpa_cli", command], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print("*** Running wpa command ***")
    print(output)

def start_server_program():
    host = socket.gethostname()
    port = 8888
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                print(data)
                if not data:
                    break
    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.bind(('127.0.0.1', port))
    # print("Waiting for a connection, host: " + host + ", port: " + str(port))

    # server_socket.listen(2)
    # conn, address = server_socket.accept()
    # print("connection From: " + str(address))
    # return conn, address


if __name__ == "__main__":
    cmd_p2p_pi("find")
    try:
        start_server_program()
        # conn, address = start_server_program()
        # try:
        #     while True:
        #         data = conn.recv(4096).decode()
        #         if data:
        #             print("From connected user: " + str(data))
        # except KeyboardInterrupt:
        #     conn.close()
        #     pass
    except KeyboardInterrupt:
        pass
    finally:
        cmd_p2p_pi("stop")
        print("Ending Program, closing connection")