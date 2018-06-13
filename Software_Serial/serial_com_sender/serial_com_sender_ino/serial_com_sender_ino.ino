//sender
#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
  // Open serial communications and wait for port to open & Arguments are speed of comm.
  Serial.begin(57600);
  mySerial.begin(9600);
  Serial.println("usb Serial");
  
}

void loop() {
  while (!Serial) {}
  
  if (Serial.available())
  {
    mySerial.println(Serial.read());
  }
  delay(1);
}
