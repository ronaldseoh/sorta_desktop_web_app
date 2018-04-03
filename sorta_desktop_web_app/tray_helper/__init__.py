__all__ = ['tray_windows', 'tray_darwin']

import platform

if platform.system() == 'Windows':
    from .tray_windows import TrayHelperController
elif platform.system() == 'Darwin':
    from .tray_macos import TrayHelperController