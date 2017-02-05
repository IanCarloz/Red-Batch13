// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin = A1;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)

void setup() {
  // put your setup code here, to run once:
// set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("SNSR OUTPUT TIME");
 
// initialize serial communications at 9600 bps:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
// set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1);
  lcd.print(analogRead(analogInPin));
  lcd.setCursor(5, 1);
  lcd.print(map(sensorValue, 0, 1023, 0, 255));
  lcd.setCursor(12, 1);
  // print the number of seconds since reset:
  lcd.print(millis() / 1000);
  
// read the analog in value:
  sensorValue = analogRead(analogInPin);
  // map it to the range of the analog out:
  outputValue = map(sensorValue, 0, 1023, 0, 255);
  // change the analog out value:
  analogWrite(analogOutPin, outputValue);

  // print the results to the serial monitor:
  Serial.print("sensor = ");
  Serial.print(sensorValue);
  Serial.print("\t output = ");
  Serial.println(outputValue);

  // wait xs before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  delay(1000);

}
