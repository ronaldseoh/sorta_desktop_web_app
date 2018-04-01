__all__ = ['tray_helper', 'flask_main']

import socket
from contextlib import closing
import webbrowser
import cherrypy

from flask_main import app

def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

if __name__ == '__main__':
    try:
        cherrypy.engine.start()

        port_number = find_free_port()

        cherrypy.tree.graft(app, "/")

        cherrypy.config.update(
            {
                'server.socket_host': '127.0.0.1',
                'server.socket_port': port_number
            }
        )

        webbrowser.open("http://127.0.0.1:" + str(port_number))
    except KeyboardInterrupt:
        cherrypy.engine.stop()