__all__ = ['tray_helper', 'flask_main']

import threading
import socket
from contextlib import closing
import webbrowser
import cherrypy

from .flask_main import app
from . import tray_helper


class ServerController(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    @staticmethod
    def find_free_port():
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.bind(('', 0))
            return s.getsockname()[1]

    def run(self):
        self.port_number = self.find_free_port()

        cherrypy.tree.graft(app, "/")

        cherrypy.config.update(
            {
                'server.socket_host': '127.0.0.1',
                'server.socket_port': self.port_number
            }
        )

        cherrypy.engine.start()

        webbrowser.open("http://127.0.0.1:" + str(self.port_number))

    def kill_server(self):
        cherrypy.engine.exit()

server_thread = ServerController()
server_thread.start()

helper_thread = tray_helper.TrayHelperController(server_thread)
helper_thread.start()
