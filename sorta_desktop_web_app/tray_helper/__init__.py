__all__ = ['tray_windows', 'tray_darwin']

import platform

if platform.system() == 'Windows':
    from sorta_desktop_web_app.tray_helper.tray_windows import TrayHelperController
elif platform.system() == 'Darwin':
    from sorta_desktop_web_app.tray_helper.tray_macos import TrayHelperController
