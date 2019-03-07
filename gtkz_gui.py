import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Kiln Control")

        grid = Gtk.Grid()
        self.add(grid)

        self.buttonP = Gtk.Button(label="P")
        self.buttonI = Gtk.Button(label="I")
        self.buttonD = Gtk.Button(label="D")
        self.buttonX = Gtk.Button(label="Imax")
        self.buttonW = Gtk.Button(label="Seconds")
        self.buttonR = Gtk.Button(label="Reset to Current Values")

        self.ato = Gtk.RadioButton.new_with_label_from_widget(None, "Auto")
        self.ato.connect("toggled", self.on_button_toggled, "Auto")

        self.man = Gtk.RadioButton.new_from_widget(self.ato)
        self.man.set_label("Manual")
        self.man.connect("toggled", self.on_button_toggled, "Manual")

        self.spinbuttonP = Gtk.SpinButton()
        self.spinbuttonI = Gtk.SpinButton()
        self.spinbuttonD = Gtk.SpinButton()
        self.spinbuttonX = Gtk.SpinButton()
        self.spinbuttonW = Gtk.SpinButton()
        self.spinbuttonM = Gtk.SpinButton()

        adjustmentP = Gtk.Adjustment(5,0,100,1,10,0)
        adjustmentI = Gtk.Adjustment(5,0,100,1,10,0)
        adjustmentD = Gtk.Adjustment(5,0,100,1,10,0)
        adjustmentW = Gtk.Adjustment(45,0,300,1,10,0)
        adjustmentX = Gtk.Adjustment(40,0,100,1,10,0)
        adjustmentM = Gtk.Adjustment(32,0,100,1,10,0)

        self.spinbuttonP.set_adjustment(adjustmentP)
        self.spinbuttonI.set_adjustment(adjustmentI)
        self.spinbuttonD.set_adjustment(adjustmentD)
        self.spinbuttonX.set_adjustment(adjustmentX)
        self.spinbuttonW.set_adjustment(adjustmentW)
        self.spinbuttonM.set_adjustment(adjustmentM)

        grid.add(self.spinbuttonP)
        grid.attach_next_to(self.spinbuttonI, self.spinbuttonP, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.spinbuttonD, self.spinbuttonI, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.spinbuttonX, self.spinbuttonD, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.spinbuttonW, self.spinbuttonX, Gtk.PositionType.BOTTOM, 1, 1)

        grid.attach_next_to(self.buttonP, self.spinbuttonP, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.buttonI, self.spinbuttonI, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.buttonD, self.spinbuttonD, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.buttonX, self.spinbuttonX, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.buttonW, self.spinbuttonW, Gtk.PositionType.RIGHT, 2, 1)

        grid.attach_next_to(self.buttonR, self.spinbuttonW, Gtk.PositionType.BOTTOM, 3, 1)

        grid.attach_next_to(self.spinbuttonM, self.buttonR, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.man, self.spinbuttonM, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.ato, self.man, Gtk.PositionType.RIGHT, 1, 1)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
