import time
import numpy as np
import requests
from gpiozero import Button

# Replace with your ThingSpeak API URL
THINGSPEAK_API_URL = "https://api.thingspeak.com/update"

def count_button_press():
    count = 0
    button = Button(17)  # Change this to your connected GPIO pin
    button_state = 0

    while True:
        if button.is_pressed:
            button_state = 1
        else:
            if button_state == 1:
                count += 1
                print(f"Button pressed {count} times.")
                generate_and_send_sine_wave(count)
                button_state = 0
        time.sleep(0.1)

def generate_and_send_sine_wave(count):
    duration = 5  # seconds
    frequency = count
    sample_rate = 1000  # Hz
    num_samples = int(sample_rate * duration)
    time_values = np.linspace(0, duration, num_samples)
    amplitude = 4096  # 12-bit DAC, change if needed

    sine_wave = (amplitude / 2) * np.sin(2 * np.pi * frequency * time_values)

    # Convert to integer values (0 to 4095) for the DAC
    sine_wave_int = (sine_wave * (4095 / amplitude)).astype(int)

    for value in sine_wave_int:
        send_to_thingspeak(value)
        time.sleep(1 / sample_rate)

def send_to_thingspeak(value):
    data = {'api_key': '35L9XLZL2G77YPIG', 'Wave': value}  # Replace with your ThingSpeak API key
    try:
        response = requests.post(THINGSPEAK_API_URL, data=data)
        if response.status_code == 200:
            print("Data sent to ThingSpeak successfully.")
        else:
            print(f"Error sending data to ThingSpeak. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data to ThingSpeak: {e}")

if __name__ == "__main__":
    try:
        print("Press the button to count and transmit sine waves.")
        count_button_press()
    except KeyboardInterrupt:
        print("Exiting...")
