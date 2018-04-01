__all__ = ['tray_windows', 'tray_darwin']

import platform

if platform.system() == 'Windows':
    from tray_windows import *
elif platform.system() == 'Darwin':
    from tray_macos import *