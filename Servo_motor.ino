int servopin = 4; //use digital pin 4
int pulse = 1500; 
unsigned short int action = 0; // False for one time change

void setup(){
    pinMode(servopin, OUTPUT);
    Serial.begin(9600);
    
    /* Controlling in the setup is for chaning the distance once*/
    digitalWrite(servopin, HIGH);
    delayMicroseconds(unsigned int); // Change the delay time for changing the angle
    digitalWrite(servopin, LOW);
    delay(20);
}

void loop(){
    if (action == 1){
    /* Controlling in the loop is for dynamically chaning the distance */
    digitalWrite(servopin, HIGH);
    delayMicroseconds(unsigned int); // Change the delay time for changing the angle
    digitalWrite(servopin, LOW);
    delay(20);
    }else{
        return;
    } 
}