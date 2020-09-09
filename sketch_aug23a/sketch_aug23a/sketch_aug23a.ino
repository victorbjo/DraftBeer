#include <Wire.h>
#include <OneWire.h>
#include <DallasTemperature.h>
// LED on pin 13
const int ledPin = 13;
char receivedMsg[13];
int byteCounter = 0;
int coolers[] = {5, 4, 7, 8, 9, 11, 12,13};
float temperature;
String mainToggle = "0";

// Data wire is plugged into port 10 on the Arduino
#define ONE_WIRE_BUS 10

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);

// arrays to hold device address
DeviceAddress airTemp =    {0x28, 0xAA, 0x79, 0x72, 0x48, 0x14, 0x01, 0x21};
DeviceAddress coolingTemp = {0x28, 0xFF, 0x7F, 0xA4, 0x52, 0x15, 0x02, 0x76};
DeviceAddress waterTemp = {0x28, 0xAA, 0x05, 0x79, 0x47, 0x14, 0x01, 0xA6};


void setup() {
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  Serial.begin(9600);
  // Call receiveEvent when data received
  Wire.onReceive(receiveEvent);

  sensors.setResolution(coolingTemp, 12);
  sensors.setResolution(waterTemp, 12);
  sensors.setResolution(airTemp, 12);


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
      mainToggle = "1";
    }
    else
    {
      digitalWrite(coolers[i - 1], tempChar[i] == 0x31); //If coolers are not set to auto, they will turn on if 
       //A value of 0x31(1) gets passed. Anything else and it will shut them off
       mainToggle = "0";
    }
  }
  String temperatureTemp0 = String(tempChar[10]);
  String temperatureTemp1 = String(tempChar[11]);
  temperature = temperatureTemp0.toInt() + (float)temperatureTemp1.toInt() / 10; //Converts the 9'th, 10'th and 11'th
  //Bytes received into a 2 digit + 1 decimal number. This is for automatic temp control
}


// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (Wire.available()) { 
    char c = Wire.read(); // receive byte as a character

    if (c == 0x01 && byteCounter == 0 || byteCounter > 0){
    
    

    receivedMsg[byteCounter] = c;
    byteCounter ++;
    //Serial.println(receivedMsg);
    if (byteCounter == 13) { //Resets byteCounter when 13 bytes has been received. Will now parse the 13 bytes
      byteCounter = 0;
      parseData(receivedMsg);
    }}

  }
}
void loop() {
delay(300);
if (byteCounter==0){
Serial.println(String(sensors.getTempC(airTemp))+":"+String(sensors.getTempC(coolingTemp))
+":"+String(sensors.getTempC(waterTemp))+":"+mainToggle+String(receivedMsg));
}

}
