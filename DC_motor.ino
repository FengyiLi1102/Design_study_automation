int MP2=10;
int pinI3=12;//define I3 interface
int pinI4=13;//define I4 interface
int power;

void setup() {
    pinMode(MP2,OUTPUT);
    pinMode(pinI3,OUTPUT);
    pinMode(pinI4,OUTPUT);
    digitalWrite(pinI4,HIGH);//turn DC Motor B move clockwise
    digitalWrite(pinI3,LOW);
    power=0;
    Serial.begin(9600);
}


void loop() {
    while (power<250) {
        power=power+10;
        Serial.println(power);
        analogWrite(MP2,power)
        delay(500);
    }
    while (power>10) {
        power=power-10;
        Serial.println(power);
        analogWrite(MP2,power)
        delay(500);
    }
}
