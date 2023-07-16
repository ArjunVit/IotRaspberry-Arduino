import tkinter as tk
import serial

def submit_value():
    try:
        value = int(entry.get())
        if value in (0, 1):
            ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with your specific COM port
            ser.write(str(value).encode())
            ser.close()
            print(f"Transmitted value: {value}")
        else:
            print("Please enter either 0 or 1.")
    except ValueError:
        print("Invalid input. Please enter either 0 or 1.")

app = tk.Tk()
app.title("Serial Transmission")

label = tk.Label(app, text="Enter 0 or 1:")
label.pack()

entry = tk.Entry(app)
entry.pack()

submit_button = tk.Button(app, text="Submit", command=submit_value)
submit_button.pack()

app.mainloop()
