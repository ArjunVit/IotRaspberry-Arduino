import serial
from gpiozero import LED

def read_serial_and_control_led():
    led = LED(17)  # Change this to your connected GPIO pin
    try:
        ser = serial.Serial('/dev/ttyS0', 9600)  # Use the appropriate serial port, '/dev/ttyS0' is for UART on Raspberry Pi 3/4
        while True:
            data = ser.readline().decode().strip()
            if data == '0':
                led.off()  # Turn off the LED
            elif data == '1':
                led.on()   # Turn on the LED
            else:
                print("Invalid value received.")
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ser.close()

if __name__ == "__main__":
    read_serial_and_control_led()
