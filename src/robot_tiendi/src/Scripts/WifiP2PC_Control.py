import socket
import subprocess
from pyp2p.net import *
from pyp2p.unl import UNL
from pyp2p.dht_msg import DHT


def cmd_p2p_pi(cmd):
    command = "p2p_" + cmd
    p = subprocess.Popen(["wpa_cli", command], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print("*** Running wpa command ***")
    print(output)

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
    cmd_p2p_pi("find")
    try:
        # conn, address = start_server_program()
        # try:
        #     while True:
        #         data = conn.recv(4096).decode()
        #         if data:
        #             print("From connected user: " + str(data))
        # except KeyboardInterrupt:
        #     conn.close()
        #     pass

        # Start Bob's direct server.
        pi_dht = DHT()
        pi_direct = Net(passive_bind="192.168.15.16", passive_port=8888, interface="wlan0", net_type="direct",
                         node_type="active", dht_node=pi_dht, debug=1)
        pi_direct.start()

        while 1:
        # Bob get reply.
            for con in pi_direct:
                for reply in con:
                    print(reply)


    except KeyboardInterrupt:
        pass
    finally:
        cmd_p2p_pi("stop")
        print("Ending Program, closing connection")