import tkinter as tk
import serial

srport = "COM7"
baud = 9600
ser = serial.Serial(srport, baud)
def turn_on():
    ser.write(b'1')
def turn_off():
    ser.write(b'0')

win = tk.Tk()
win.title('LED Control')
on = tk.Button(win, text="Turn On", command=turn_on)
off = tk.Button(win, text="Turn Off", command=turn_off)
on.pack()
off.pack()
win.mainloop()
