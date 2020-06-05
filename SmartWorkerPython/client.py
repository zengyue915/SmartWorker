
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

class Client:
    def __int__(self):
        self.soc = None
        self.conn = None
        self.addr = None

    def connect(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.soc.connect((HOST, PORT))

        self.soc.sendall(b'Connect')
        data = self.soc.recv(1024)
        msg = data.decode("utf-8")
        print('-', msg)




    def close(self):
        self.soc.sendall(b"Close Connection")




    def requestVideo(self, videoid):
        # videoid = 0
        self.soc.sendall(b"Video 111")

        n = "received"
        conn, addr = self.soc.accept()
        while True:
            i = 0
            buffer = conn.recv(1024)
            with open('received.mp4', "wb") as video:
                while buffer:
                    video.write(buffer)
                    print("buffer {0}".format(i))
                    buffer = self.conn.recv(1024)
                    i += 1
        print("Done")



    def requestVideo2(self, videoid):
        # videoid = 0
        self.soc.sendall(b"Video 111")

        while True:
            i = 0
            buffer = self.soc.recv(1024)
            with open('received.mp4', "wb") as video:
                while buffer:
                    video.write(buffer)
                    print("buffer {0}".format(i))
                    buffer = self.soc.recv(1024)
                    i += 1



client = Client()
client.connect()
# print('1')
# client.requestVideo(111)
client.requestVideo2(123)
client.close()
