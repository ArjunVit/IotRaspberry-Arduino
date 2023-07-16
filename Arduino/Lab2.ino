#include<Wifi.h?
#include<UnoWifiDeved.h>

#define baud 9600

WifiData espserial;

void setup() {
    Serial.begin();
    pinMode(13, OUTPUT);
    digitalWrite(13,LOW);
    espserial.begin(baud);
}

void loop() {
    while(Serial.available) {
        char inchar = (char) serial.read();
        espserial.write(inchar);
    }
    while(espserial.available) {
        char inchar = (char) espserial.read();
        Serial.write(inchar);
    }
}
