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
 by Tom Igoe
 
 This example code is in the public domain.
 
 */

// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 13; // Analog output pin that the LED is attached to

const int di= 200;
const int charPause= 300;
const int wordPause= 400;

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)
String a ;
void setup() {
  
  // initialize serial communications at 9600 bps:
  Serial.begin(9600); 
}

void loop() {
  // read the analog in value:
  sensorValue = analogRead(analogInPin);            
  // map it to the range of the analog out:
  outputValue = map(sensorValue, 0, 1023, 0, 255);  
  // change the analog out value:
  analogWrite(analogOutPin, outputValue);           
  //Morse(".../---/...");  
  
  // print the results to the serial monitor:
  
  //Serial.write("lol");
  a = Serial.readStringUntil('\n');
  Serial.println(a);
  Morse(a);
  //Serial.print(Serial.read());
  /*
  Serial.print("sensor = " );                       
  Serial.print(sensorValue);      
  Serial.print("\t output = ");      
  Serial.println(outputValue);   
//*/
  // wait 2 milliseconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  delay(2);                     
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
      tone(13, 440, 2*di);
//      delay(2*di);
//      digitalWrite(analogOutPin, 0); 
//       noTone();
      delay(2*di);
    }
    if( A.charAt(i)=='/')
    {
    delay(charPause);
    }
    if( A.charAt(i)==' ')
    {
    delay(wordPause);
    }
  }
}
 

