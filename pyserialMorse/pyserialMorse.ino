/*
  Analog input, analog output, serial output
 
 Reads an analog input pin, maps the result to a range from 0 to 255
 and uses the result to set the pulsewidth modulation (PWM) of an output pin.
 Also prints the results to the serial monitor.
 
 The circuit:
 * potentiometer connected to analog pin 0.
   Center pin of the potentiometer goes to the analog pin.
   side pins of the potentiometer go to +5V and ground
 * LED connected from digital pin 9 to ground
 
 created 29 Dec. 2008
 modified 9 Apr 2012
 by Tom Igoe (pruit????)
 
 This example code is in the public domain.
 
 */

// These constants won't change.  They're used to give names
// to the pins used:
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
void setup() {
     
  Serial.begin(9600);
  digitalWrite(analogOutPin,HIGH);
 // analogWrite(A0,HIGH);
  //di=Serial.readStringUntil('\n').toInt();
  di=50;// make same as python if above line doesn't work
  da=3*di;//as I suspect it won't
  
}
void loop() {
  // read the analog in value:
  //sensorValue = analogRead(analogInPin);            
  // map it to the range of the analog out:
 // outputValue = map(sensorValue, 0, 1023, 0, 255);  
  // change the analog out value:
 // analogWrite(analogOutPin, outputValue);           
  //Morse(".../---/...");  
//  /*
//  print(digitalRead(inPin));
 if( digitalRead(inPin)==LOW)
 {
    Serial.print("+");
    //up=false;
 }
 else if (digitalRead(inPin)==HIGH//&&!up)
 )
 {
    Serial.print("-");
    //up=true;
 }

// */
  // print the results to the serial monitor:
  //Serial.write("lol");
  a = Serial.readStringUntil('\n');
  Serial.println(a);// is this neccesary? isn't a already written in Serial?
  if(a!="+"||a!="-")
    Morse(a);
  //Serial.print(Serial.read());
  /*//kinda part of another project at this point
  Serial.print("sensor = " );                       
  Serial.print(sensorValue);      
  Serial.print("\t output = ");      
  Serial.println(outputValue);   
//*/
  // wait 2 milliseconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  delay(di);                     
}
void Morse(String A)
{
  for(int i=0; i<A.length(); i++)
  {
    if( A.charAt(i)=='.')
    {
//      digitalWrite(analogOutPin, outputValue);      
//      delay(di);
//      digitalWrite(analogOutPin, 0);
      tone(13,440,di);
//      noTone();
     delay(di); 
    }
    if( A.charAt(i)=='-')
    {
//       digitalWrite(analogOutPin, outputValue);      
      tone(13, 440, da);
//      delay(2*di);
//      digitalWrite(analogOutPin, 0); 
//       noTone();
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
 

