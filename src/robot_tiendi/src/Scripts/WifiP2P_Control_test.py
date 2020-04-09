import socket
import subprocess
import SocketServer
import threading


from MoveMotors import MoveMotors



HOST = "192.168.15.16"
PORT = 8888
SPEEDL = 180
SPEEDR = SPEEDL

DIRECTION = "s"


class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        DIRECTION = str(self.data)
        # print '=== Got something from ' + self.client_address[0] + ' ==='
        # print(self.data) # Testing purposes




def cmd_p2p_pi(cmd):
    command = "p2p_" + cmd
    p = subprocess.Popen(["wpa_cli", command], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print("*** Running wpa command ***")
    print(output)

def start_server_program():
    server_socket = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    print("Waiting for a connection, host: " + HOST + ", port: " + str(PORT))
    server_socket.serve_forever()


if __name__ == "__main__":
    cmd_p2p_pi("find")
    robot = MoveMotors()

    try:
        server = threading.Thread(target=start_server_program(), args=(1, ))
        rbt = threading.Thread(target=robot.robotMovement(DIRECTION), args=(1, ))
    except KeyboardInterrupt:
        pass
    finally:
        cmd_p2p_pi("stop")
        print("Ending Program, closing connection")
