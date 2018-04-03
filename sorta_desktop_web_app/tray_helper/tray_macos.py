import webbrowser
import rumps

from sorta_desktop_web_app.server_controller import ServerController

class TrayHelperController(rumps.App):

    def __init__(self):
        rumps.App.__init__(
            self,
            'sorta',
            quit_button=None
        )

        self.__server_controller = ServerController()
    
    @rumps.clicked("Preferences")
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")

    @rumps.clicked("Silly button")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

    @rumps.clicked('Quit')
    def stop_app(self, _):
        self.__server_controller.stop_server()
        rumps.quit_application()

    def start_app(self):
        # Start the server
        self._port_number = self.__server_controller.start_server()

        webbrowser.open("http://127.0.0.1:" + str(self._port_number))

        rumps.App.run(self)
