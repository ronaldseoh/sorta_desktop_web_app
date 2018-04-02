import threading
import infi.systray


class TrayHelperController(threading.Thread):

    def __init__(self, server_thread):
        threading.Thread.__init__(self)

        self.server_thread = server_thread
        self.server_thread.join()

        self.menu_options = (
            ("Say Hello", None, self.say_hello),
        )

        self.systray = infi.systray.SysTrayIcon(
            "icon.ico",
            "Example tray icon",
            self.menu_options,
            on_quit=self.kill_threads
        )

    def say_hello(self, systray):
        print("Hello, World!")

    def kill_threads(self, systray):
        self.server_thread.kill_server()

    def run(self):
        self.systray.start()