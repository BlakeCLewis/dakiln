import gi
import mypid

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self, butt):
        Gtk.Window.__init__(self, title="Kiln Control")

        grid = Gtk.Grid()
        self.add(grid)

        self.duh = butt

        self.buttonC = Gtk.Button(label="C")
        self.buttonC.connect("clicked", self.C_press)
        self.buttonP = Gtk.Button(label="P")
        self.buttonP.connect("clicked", self.P_press)
        self.buttonI = Gtk.Button(label="I")
        self.buttonI.connect("clicked", self.I_press)
        self.buttonD = Gtk.Button(label="D")
        self.buttonD.connect("clicked", self.D_press)
        self.buttonX = Gtk.Button(label="Imax")
        self.buttonX.connect("clicked", self.X_press)
        self.buttonW = Gtk.Button(label="Seconds")
        self.buttonW.connect("clicked", self.W_press)

        self.buttonR = Gtk.Button(label="Reset to Current Values")
        self.buttonR.connect("clicked", self.R_press)

        self.ato = Gtk.RadioButton.new_with_label_from_widget(None, "Auto")
        self.ato.connect("toggled", self.on_button_toggled, "Auto")

        self.man = Gtk.RadioButton.new_from_widget(self.ato)
        self.man.set_label("Manual")
        self.man.connect("toggled", self.on_button_toggled, "Manual")

        self.spinbuttonC = Gtk.SpinButton()
        self.spinbuttonP = Gtk.SpinButton()
        self.spinbuttonI = Gtk.SpinButton()
        self.spinbuttonD = Gtk.SpinButton()
        self.spinbuttonX = Gtk.SpinButton()
        self.spinbuttonW = Gtk.SpinButton()
        self.spinbuttonM = Gtk.SpinButton()

        self.adjustmentC = Gtk.Adjustment(self.duh.getKc(),0,100,1,10,0)
        self.adjustmentP = Gtk.Adjustment(self.duh.getKp(),0,100,1,10,0)
        self.adjustmentI = Gtk.Adjustment(self.duh.getKi(),0,100,1,10,0)
        self.adjustmentD = Gtk.Adjustment(self.duh.getKd(),0,100,1,10,0)
        self.adjustmentW = Gtk.Adjustment(self.duh.getWin(),0,300,1,10,0)
        self.adjustmentX = Gtk.Adjustment(self.duh.getImax(),0,100,1,10,0)
        self.adjustmentM = Gtk.Adjustment(32,0,100,1,10,0)

        self.spinbuttonC.set_adjustment(self.adjustmentC)
        self.spinbuttonP.set_adjustment(self.adjustmentP)
        self.spinbuttonI.set_adjustment(self.adjustmentI)
        self.spinbuttonD.set_adjustment(self.adjustmentD)
        self.spinbuttonX.set_adjustment(self.adjustmentX)
        self.spinbuttonW.set_adjustment(self.adjustmentW)
        self.spinbuttonM.set_adjustment(self.adjustmentM)

        grid.add(self.spinbuttonC)
        grid.attach_next_to(self.spinbuttonP, self.spinbuttonC, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.spinbuttonI, self.spinbuttonP, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.spinbuttonD, self.spinbuttonI, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.spinbuttonX, self.spinbuttonD, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.spinbuttonW, self.spinbuttonX, Gtk.PositionType.BOTTOM, 1, 1)

        grid.attach_next_to(self.buttonC, self.spinbuttonC, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.buttonP, self.spinbuttonP, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.buttonI, self.spinbuttonI, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.buttonD, self.spinbuttonD, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.buttonX, self.spinbuttonX, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.buttonW, self.spinbuttonW, Gtk.PositionType.RIGHT, 2, 1)

        grid.attach_next_to(self.buttonR, self.spinbuttonW, Gtk.PositionType.BOTTOM, 3, 1)

        grid.attach_next_to(self.spinbuttonM, self.buttonR, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.man, self.spinbuttonM, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.ato, self.man, Gtk.PositionType.RIGHT, 1, 1)



    def C_press(self, button):
        self.duh.setKc(self.adjustmentC.get_value())
        print(self.duh.getKc())
    def P_press(self, button):
        self.duh.setKp(self.adjustmentP.get_value())
        print(self.duh.getKp())
    def I_press(self, button):
        self.duh.setKi(self.adjustmentI.get_value())
        print(self.duh.getKi())
    def D_press(self, button):
        self.duh.setKd(self.adjustmentD.get_value())
        print(self.duh.getKd())
    def X_press(self, button):
        self.duh.setImax(self.adjustmentX.get_value())
        print(self.duh.getImax())
    def W_press(self, button):
        self.duh.setWin(self.adjustmentW.get_value())
        print(self.duh.getWin())
    def R_press(self, button):
        self.spinbuttonC.set_value(self.duh.getKc())
        self.spinbuttonP.set_value(self.duh.getKp())
        self.spinbuttonI.set_value(self.duh.getKi())
        self.spinbuttonD.set_value(self.duh.getKd())
        self.spinbuttonW.set_value(self.duh.getWin())
        self.spinbuttonX.set_value(self.duh.getImax())

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

output = mypid.mypid(100)
win = GridWindow(output)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
