import pyscreenshot as ImageGrab
import datetime

import pyHook
import pythoncom
from pynput.keyboard import Key, Listener
from pynput import keyboard


def on_keypress(key):
    d_date = datetime.datetime.now()
    reg_format_date = d_date.strftime("%d-%m-%Y %I-%M-%S %p")
    print(key)

    im = ImageGrab.grab()
    im.save(reg_format_date+'.jpg')


key_listener = keyboard.Listener(on_release=on_keypress)
key_listener.start()

def onclick(event):
	d_date = datetime.datetime.now()
	reg_format_date = d_date.strftime("%d-%m-%Y %I-%M-%S %p")

	print (event.Position)

	im = ImageGrab.grab()
	im.save(reg_format_date+'.jpg')
	return True


def main():
	hm = pyHook.HookManager()
	hm.SubscribeMouseAllButtonsDown(onclick)
	hm.HookMouse()
	pythoncom.PumpMessages()
	hm.UnhookMouse()



if __name__ == "__main__":
    main()



