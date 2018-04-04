__all__ = ['tray_helper', 'server_controller', 'flask_main']

from sorta_desktop import tray_helper
from sorta_desktop import server_controller
from sorta_desktop import flask_main

def start_with_tray_helper():

    helper = tray_helper.TrayHelperController()

    helper.start_app()
