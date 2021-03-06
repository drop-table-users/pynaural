import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from threading import Thread
from main import GENERATOR


def show_object(widget, data):
    data.show_all()

def hide_object(widget, data):
    data.hide()


def dialog_run(widget, data):
    data.run()
    data.hide()


def full_quit(widget):
    gtk.main_quit()
    exit(0)


def pause(widget):
    global GENERATOR
    GENERATOR.pause()


def create_and_play(widget, data):
    carrier_box   = data[0]
    beat_box      = data[1] ## boots n cats n boots n cats
    duration_box  = data[2]
    volume_adjust = data[3]

    carrier_freq  = float(carrier_box.get_text())
    beat_freq     = float(beat_box.get_text())
    duration      = int(round(float(duration_box.get_text()), 0))
    volume        = int(volume_adjust.get_value()) / 100

    global GENERATOR
    GENERATOR.__init__(carrier=carrier_freq, duration=duration, beat_freq=beat_freq, vol=volume)

    t = Thread(target=GENERATOR.play)
    t.daemon = True
    t.start()


def update_volume(widget, data):
    volume = int(data.get_value()) / 100

    global GENERATOR
    GENERATOR.vol = volume
    GENERATOR.pause()
    GENERATOR.play()
