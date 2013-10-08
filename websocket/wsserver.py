import socket
import thread

from websocket import config, wsclient


class Server:
    """
    Initializes server that will store client connections
    """
    def __init__(self):
        self.clients = []

    def run(self):
        """
        Starts the server
        """
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', config.socket_port))
        s.listen(1)

        try:
            while 1:
                conn, addr = s.accept()
                print('New client connected', addr)

                newClient = wsclient.Client(conn, addr, self)
                thread.start_new_thread(newClient.run())

                self.clients.append(newClient)
        except KeyboardInterrupt:
            [client.close() for client in self.clients]
            s.close()

    def remove(self, client):
        """
        Removes a client
        """
        self.clients.remove(client)

    def send_to_all(self, data):
        """
        Sends a message to all clients
        """
        [client.send(data) for client in self.clients]