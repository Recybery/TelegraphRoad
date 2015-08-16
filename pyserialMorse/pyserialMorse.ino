const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 13; // Analog output pin that the LED is attached to
const int inPin= 7;
int di;
int da;
const int wordPause= 7*di;
boolean up=false;

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)
String a ;
int out =0;
void setup() {
  Serial.begin(9600);
  digitalWrite(analogOutPin,HIGH);
  di=100;
  da=3*di;
}
void loop() {
 if (digitalRead(inPin)==HIGH)
 {
    Serial.print("+");
    up=true;
 }
 else if( digitalRead(inPin)==LOW&&up)
 {
    Serial.print("_");
    up=false;
 }                  
}
void Morse(String A)
{
  for(int i=0; i<A.length(); i++)
  {
    if( A.charAt(i)=='.')
    {
      tone(13,440,di);
     delay(di); 
    }
    if( A.charAt(i)=='-')
    {     
      tone(13, 440, da);
      delay(da);
    }
    if( A.charAt(i)=='/')
    {
    delay(da);
    }
    if( A.charAt(i)==' ')
    {
    delay(wordPause);
    }
  }
}
 

