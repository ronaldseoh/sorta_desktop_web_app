import webbrowser
import infi.systray

from ..server_controller import ServerController


class TrayHelperController():

    def __init__(self):
        self.__menu_options = (
            ("Say Hello", None, self.say_hello),
        )

        self.__systray = infi.systray.SysTrayIcon(
            "icon.ico",
            "Example tray icon",
            self.__menu_options,
            on_quit=self.stop_app
        )

        self.__server_controller = ServerController()

    def say_hello(self, systray):
        print("Hello, World!")

    def stop_app(self, systray):
        self.__server_controller.stop_server()

    def start_app(self):
        # Start tray helper first
        self.__systray.start()

        # Start the server
        self._port_number = self.__server_controller.start_server()

        webbrowser.open("http://127.0.0.1:" + str(self._port_number))
