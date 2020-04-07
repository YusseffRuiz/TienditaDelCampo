import socket
import subprocess
import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):

    firstFixFlag = False # this will go true after the first GPS fix.
    firstFixDate = ""
    DEBUG = True
    SLEEP = 1
    def handle(self):
        # Get the JSON data...return the ESSIDS (their respective MAC addresses and the signal strength)
        # self.data = json.loads(self.request.recv(1024).strip())
        self.data = self.request.recv(1024).strip()
        print '=== Got something from ' + self.client_address[0] + ' ==='
        print self.data # Print it out I guess...just to note it's been received
        print '\n\n\n=== SENDING SPOOFED DATA TO ALL CLIENTS ===\n'
  #      self.request.sendall(json.dumps({'location': {'lat': self.latitude, 'lng': self.longtitude}, 'accuracy': self.accuracy}))
#        print json.dumps({'location': {'lat': self.latitude, 'lng': self.longtitude}, 'accuracy': self.accuracy})


def cmd_p2p_pi(cmd):
    command = "p2p_" + cmd
    p = subprocess.Popen(["wpa_cli", command], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print("*** Running wpa command ***")
    print(output)

def start_server_program():
    host = socket.gethostname()
    port = 8888
#    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    server_socket.bind(('', port))
    server_socket = SocketServer.TCPServer(("", 8888), MyTCPHandler)
    print("Waiting for a connection, host: " + host + ", port: " + str(port))
    server_socket.serve_forever()

#    server_socket.listen(10)
#    print("Socket listening")
#    while(True):
#    	conn, address = server_socket.accept()
#    print("connection From: " + str(address))
#    return conn, address


if __name__ == "__main__":
    cmd_p2p_pi("find")
    try:
        start_server_program()
        try:
            while True:
                data = conn.recv(4096).decode()
                if data:
                    print("From connected user: " + str(data))
        except KeyboardInterrupt:
            conn.close()
            pass
    except KeyboardInterrupt:
        pass
    finally:
        cmd_p2p_pi("stop")
        print("Ending Program, closing connection")
