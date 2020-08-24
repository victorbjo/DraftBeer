#include <Wire.h>

// LED on pin 13
const int ledPin = 13;
char receivedMsg[13];
int byteCounter = 0;
int coolers[] = {6, 7, 8, 9, 10, 11, 12, 13};
float temperature;
void setup() {
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  Serial.begin(4800);
  // Call receiveEvent when data received
  Wire.onReceive(receiveEvent);

  // Setup pin 13 as output and turn LED off
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}


void parseData(char tempChar[])
{
  for (int i = 1; i < 9; i ++)
  {
    if (tempChar[i] == 0x33)
    {
      //If tempChar 1-8 = 3, then the arduino shall control the heaters
    }
    else
    {
      digitalWrite(coolers[i - 1], tempChar[i] == 0x31); //If coolers are not set to auto, they will turn on if 
       //A value of 0x31(1) gets passed. Anything else and it will shut them off
    }
  }
  String temperatureTemp0 = String(tempChar[10]);
  String temperatureTemp1 = String(tempChar[9]);
  String temperatureTemp2 = String(tempChar[11]);
  temperature = temperatureTemp0.toInt();
  temperature = temperature + temperatureTemp1.toInt() * 10 + (float)temperatureTemp2.toInt() / 10; //Converts the 9'th, 10'th and 11'th
  //Bytes received into a 2 digit + 1 decimal number. This is for automatic temp control
}


// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (Wire.available()) { 
    char c = Wire.read(); // receive byte as a character
    receivedMsg[byteCounter] = c;
    byteCounter ++;
    if (byteCounter == 13) { //Resets byteCounter when 13 bytes has been received. Will now parse the 13 bytes
      byteCounter = 0;
      parseData(receivedMsg);
    }

  }
}
void loop() {
  delay(400);

}
