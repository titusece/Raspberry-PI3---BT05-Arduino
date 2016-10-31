int ledPin = 13;
 
void setup() {
  Serial.begin( 9600 );    // 9600 is the default baud rate for the serial Bluetooth module
}
 
void loop() {
  // listen for the data
  if ( Serial.available() > 0 ) {
    // read a numbers from serial port
    int count = Serial.parseInt();
    
     // print out the received number
    if (count > 0) {
        Serial.print("Raspberry PI3 board send : ");
        Serial.println(String(count));
        // blink the LED
        blinkLED(count);
    }
  }
}
 
void blinkLED(int count) {
  for (int i=0; i< count; i++) {
    digitalWrite(ledPin, HIGH);
    delay(1000);
    digitalWrite(ledPin, LOW);
    delay(1000);
  } 
}
