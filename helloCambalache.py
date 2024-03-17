import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)


    def on_activate(self, app):
        # Create a Builder
        builder = Gtk.Builder()
        builder.add_from_file("deepfake-tts.ui")

        # Obtain the button widget and connect it to a function
        button = builder.get_object("button1")
        button.connect("clicked", self.hello)

        # Obtain and show the main windows
        self.win = builder.get_object("main_window")
        self.win.set_application(self)
        self.win.present()

    def hello(self, button):
        print("Hello")


app = MyApp(application_id="deepfake-tts")
app.run(sys.argv)

