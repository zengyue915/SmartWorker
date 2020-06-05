import socket

HOST = '127.0.0.1'
PORT = 65432
buffer = 1024

Succeed = False

class Server:
    def __init__(self, host, port, buffer_size):
        self.HOST = host
        self.PORT = port
        self.BUFFER = buffer_size
        self.conn = None
        self.address = None
        self.soc = None


    def serverStart(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.bind((self.HOST, self.PORT))
        self.soc.listen()
        print("Server Ready")

#
#    def processRequest(self):
#        conn, addr = self.soc.accept()
#        print('Connected by', addr)
#        while True:
#            data = conn.recv(self.BUFFER)
#            msg = data.decode("utf-8")
#            print("Request: " + msg)
#            if msg == "Connect":
#                conn.sendall(b'Success')
#            elif msg == "Close Connection":
#                print("Connection Closed by the client")
#                break
#
#            # elif msg.startsWith("Video"):
#            #     videoid = int(msg.rstrip("Video"))
#            #     self.sendVideo(videoid)
#
#            elif msg[:5] == 'Video':
#                videoid = int(msg.split()[1])
#                self.sendVideo(videoid)
#
#            elif not data:
#                break
#
#            else:
#                print('else????')



    def processRequest2(self):
        self.conn, self.addr = self.soc.accept()
        print('Connected by', self.addr)
        while True:
            data = self.conn.recv(self.BUFFER)
            msg = data.decode("utf-8")
            print("Request: " + msg)
            if msg == "Connect":
                self.conn.sendall(b'Success')
            elif msg == "Close Connection":
                print("Connection Closed by the client")
                break

            # elif msg.startsWith("Video"):
            #     videoid = int(msg.rstrip("Video"))
            #     self.sendVideo(videoid)

            elif msg[:5] == 'Video':
                videoid = int(msg.split()[1])
                self.sendVideo(videoid)
                break

            elif not data:
                break

            else:
                print('else????')


    def sendVideo(self, videoid):
        print("Sending video " + str(videoid))
        # buf = b'fakeVideo'
        # print(buf)
        # self.conn.sendall(buf)


        with open("Sample.mp4", "rb") as video:
            buf = video.read()
            self.conn.sendall(buf)







server = Server(HOST, PORT, buffer)
server.serverStart()
# server.processRequest()
server.processRequest2()


