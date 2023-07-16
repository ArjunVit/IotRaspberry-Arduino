from picamera import PiCamera
from gpizero import LED, Button

cam = PiCamera()
led = LED(4)
but = Button(17)
while True:
    but.wait_for_press()
    cam.capture('/home/Pi/desktop/image.jpg')
    led.on()
    but.wait_for_release()
    led.off()
