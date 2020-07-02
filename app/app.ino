const int pinLed = 13;

void setup() {
    pinMode(pinLed, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        if (Serial.readString() == "Mask") {
            digitalWrite(pinLed, HIGH);
            Serial.println("funka :D");
        } else {
            digitalWrite(pinLed, LOW);
        }
    }
    //delay(1000);
}
