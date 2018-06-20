// bit from char in reverse order
// sender
int tx=10;
int output[8];
char c='A';
int i;
int p=0;
void setup()
{
  Serial.begin(57600);
  pinMode(tx,OUTPUT);
}


void loop()
{ 
  for (i = 0; i <=8 ; ++i) 
  {
    output[i] = (c >> i) & 1;
  }
  i=0;
  while(i<=8)
  {
    Serial.println(output[i]);
    if (output[i]==1)
    {
      digitalWrite(tx,HIGH);
      delay(1000);
    }
    else
    {
      digitalWrite(tx,LOW);
    }
    i++;
  }
  delay(1000);
}



