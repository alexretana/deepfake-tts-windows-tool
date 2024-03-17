import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # add boxes for layout
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)


        # add button for layout
        self.button = Gtk.Button(label="Hello")
        self.button.connect('clicked', self.hello)

        # build hierarchy
        self.set_child(self.box1)
        self.box1.append(self.box2)
        self.box1.append(self.box3)

        self.box2.append(self.button)

        self.check = Gtk.CheckButton(label="And goodbye?")
        self.box2.append(self.check)

        # adding switch
        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        
        self.switch = Gtk.Switch()
        self.switch.set_active(False)
        self.switch.connect("state-set", self.switch_switched)

        self.switch_box.append(self.switch)
        self.box2.append(self.switch_box)
        
        self.label = Gtk.Label(label="A switch")
        self.switch_box.append(self.label)
        self.switch_box.set_spacing(5)

        # add title
        self.set_title("HelloGTK")

    def hello(self, button):
        print("Hello World")
        if self.check.get_active():
            print("Goodbye world!")
            self.close()

    def switch_switched(self, switch, state):
        print(f"The switch has ben switched {'on' if state else 'off'}")
     
 
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win =MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
