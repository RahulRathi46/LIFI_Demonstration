// bit from char in reverse order
// sender
int rx=11;
int i;

void setup()
{
  Serial.begin(57600);
  pinMode(rx,INPUT);
}

void loop()
{ 
  i=0;
  Serial.println("new");
  while(i<=8)
  {
    if (digitalRead(rx)==HIGH)
    {
      Serial.println("1");
      delay(1000);
    }
    else
    {
      Serial.println("0");
    }
    i++;
  }
  Serial.flush();
  delay(1000);
}




