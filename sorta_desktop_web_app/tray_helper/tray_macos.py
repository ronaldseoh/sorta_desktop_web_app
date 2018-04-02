import threading
import rumps

class TrayHelperController(threading.Thread, rumps.App):

    def __init__(self, server_thread):
        threading.Thread.__init__(self)

        rumps.App.__init__(self, "sorta_desktop")

        self.server_thread = server_thread
    
    @rumps.clicked("Preferences")
    def prefs(self, _):
        rumps.alert("jk! no preferences available!")

    @rumps.clicked("Silly button")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked("Say hi")
    def sayhi(self, _):
        rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

    @rumps.quit_application("Quit")
    def kill_threads(self, _):
        self.server_thread.kill_server()

    def run(self):
        self.run()
