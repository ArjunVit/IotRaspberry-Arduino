#include "thingProperties.h"

void setup() {
    Serial.begin(9600)
    delay(1500);
    initProperties();
    pinMode(LED_BUILTIN, OUTPUT);
    ArduinoCloud.begin(ArduinoIoTprefferedConnection);
    setDebugMessageLevel(2);
    ArduinoCloud.print(DebugInfo);
}

void loop() {
    ArduinoCloud.update();
}

void onLEDChange() {
    if(s == 1) {
        digitalWrite(LED_BUILTIN, HIGH);
    } else {
        digitalWrite(LED_BUILTIN, LOW);
    }
}
