__all__ = ['tray_helper', 'server_controller', 'flask_main']

from . import tray_helper

helper = tray_helper.TrayHelperController()
helper.start_app()
