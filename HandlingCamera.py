import cv2
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)

class takePicture:
    def on_window_destroy(self, *args):
        Gtk.main_quit()
    
    def on_btnSave_clicked(self, *args):
        txtName = builder.get_object("txtName")
        Name = (txtName.get_text())
        
        if (txtName.get_text() == ""):
            dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonType.OK, "Name cannot be empty")
            dialog.run()
            dialog.destroy()
        else:
            ret, frame = capture.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite("gambar/"+Name+".jpg", frame)
            image2.set_from_file("gambar/"+Name+".jpg")
            
def show_frame(*args):
    ret, frame = capture.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    framecp = frame.copy()
    
    pb = GdkPixbuf.Pixbuf.new_from_data(framecp.tobytes(),
    GdkPixbuf.Colorspace.RGB,
    False,
    8,
    framecp.shape[1],
    framecp.shape[0],
    framecp.shape[2]*framecp.shape[1])
    
    image1.set_from_pixbuf(pb.copy())
    return True
    
builder = Gtk.Builder()
builder.add_from_file("/home/pi/programming/handling-camera/HandlingCamera.glade")
window = builder.get_object("window")
image1 = builder.get_object("image1")
image2 = builder.get_object("image2")
window.show_all()

builder.connect_signals(takePicture())
GLib.idle_add(show_frame)
Gtk.main()