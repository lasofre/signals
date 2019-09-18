byte senal;
byte integral;
byte t1=B0000000;
byte ti=B0000000;
byte t2=B0000000;
void setup() {
  DDRD = B11111111; //Configuro puerto D como salida pines (0-7)
  pinMode(A0,INPUT);//Configuro A0 como entrada analogica
}

void loop() {
  t1=millis();
  senal=analogRead(A0);
  if(senal>B10000000)integral+=senal*(ti-t2);
  else integral-=senal*(ti-t2);
  ti=t1;
  PORTD = integral;
  t2=millis();
}
