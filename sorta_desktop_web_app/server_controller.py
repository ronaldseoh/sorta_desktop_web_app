import socket
from contextlib import closing
import cherrypy

from sorta_desktop_web_app import flask_main


class ServerController():

    def start_server(self):
        self._port_number = self.find_free_port()

        cherrypy.tree.graft(flask_main.app, "/")

        cherrypy.config.update(
            {
                'server.socket_host': '127.0.0.1',
                'server.socket_port': self._port_number
            }
        )

        cherrypy.engine.start()

        return self._port_number

    def stop_server(self):
        cherrypy.engine.exit()

    @staticmethod
    def find_free_port():
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.bind(('', 0))
            return s.getsockname()[1]
