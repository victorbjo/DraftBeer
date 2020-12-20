#include <SoftwareSerial.h>
SoftwareSerial mySerial(12, 11);
int receivedMsg[40];
int start[] = {255,255,253,0};
bool validStart = false;
int counter = 0;
bool autopilot = 1;
float goalTemp = 2;
void setup() {
  // put your setup code here, to run once:

Serial.begin(57600);
mySerial.begin(57600);
}

void sendTmp(){
  uint8_t msg[] = {0xff,0xff,0xfd,0x00,0x0d,0x1,0x9,0x08,0x10,0x34,0x1,0x2,0xfe};
  mySerial.write(msg, sizeof(msg));
  Serial.write("Sending new pckg back");
}
void sendStatus(){
  uint8_t msg[] = {0xff,0xff,0xfd,0x00,0x0d,0x1,0x0,0x1,0x1,0x0,0x0,0x00,0xfe};
  mySerial.write(msg, sizeof(msg));
  Serial.write("Sending new pckg back");
}
void ChangeUnits(int units[]){
  Serial.println("");
  if (autopilot == false){
  for(byte i = 0; i < 6; i++){
    
    Serial.println(units[i]);
  }}

}
void ChangeMode(int mode[]){
  Serial.println();
  autopilot = mode[0];
  autopilot == false? Serial.println("Autopilot disengaged"):Serial.println("Autopilot Engaged");
  goalTemp = mode[1];
  goalTemp += float(mode[2])/100;
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
    }else{
    if(autopilot){
      Serial.println(goalTemp);
      delay(1000);
    }
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
            if (Msg[receivedMsg[4]-1] == 254){
              Serial.println();
              Serial.print("Complete Package with length ");
              Serial.print(Msg[4]);
              Serial.print("; Instruction: ");
              Serial.print(Msg[5]);
              Serial.print("; Params: ");
              int params[Msg[4]-7];
              for(int i = 6; i < Msg[4]-1; i++){
                params[i-6] = Msg[i];
                Serial.print(params[i-6]);
              }
               switch (Msg[5]){
                case 1:
                  sendTmp();
                  break;
                case 2:
                  sendStatus();
                  break;
                case 3:
                  ChangeUnits(params);
                  break;
                case 4:
                  ChangeMode(params);
                default:
                  break;
                
              }
            }
            counter = 0;
            Serial.println();
            return false;
          
        
      }
      }
      }
      }
      }
  //erial.println(counter);
  //mySerial.write("Test\n");
 // delay(5);
}
