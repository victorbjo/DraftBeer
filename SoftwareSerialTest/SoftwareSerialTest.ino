#include <SoftwareSerial.h>
SoftwareSerial mySerial(12, 11);
int receivedMsg[40];
int start[] = {255,255,253,0};
bool validStart = false;
int counter = 0;
void setup() {
  // put your setup code here, to run once:

Serial.begin(57600);
mySerial.begin(57600);
}

void loop() {
  // put your main code here, to run repeatedly:
      //Serial.println("OK");
  if (mySerial.available()>0)
    {
    receivedMsg[counter] =  mySerial.read();
    Serial.print(receivedMsg[counter]);
    Serial.print("; ");
    counter++;
    }
    if (counter == 5){
      validStart = true;
      for(int i = 0; i < 4; i++){
        if (receivedMsg[i] != start[i]){
          validStart = false;
        }
      }
      //Serial.print(validStart);
      if (validStart == false){
        while (mySerial.available()>0){
          receivedMsg[counter] =  mySerial.read();
         }
      Serial.println("THE");
      counter = 0;
      }else{
        int Msg[receivedMsg[4]];
        for(int i = 0; i < 5; i++){
         Msg[i] = receivedMsg[i];
        }
        while (true){
          if (mySerial.available()>0){
          Msg[counter] =  mySerial.read();
          Serial.print(Msg[counter]);
          Serial.print("; ");
          counter++;
          if (counter == receivedMsg[4]){
            if (Msg[counter-1] == 254){
              Serial.println();
              Serial.print("Complete Package with length ");
              Serial.print(Msg[4]);
              Serial.print("; Instruction: ");
              Serial.print(Msg[5]);
              Serial.print("; Params: ");
              for(int i = 6; i < Msg[4]-1; i++){
                Serial.print(Msg[i]);
              }
            }
            counter = 0;
            Serial.println();
            return false;
          }
        }}
      }
      
    }
    

  //erial.println(counter);
  //mySerial.write("Test\n");
 // delay(5);
}
