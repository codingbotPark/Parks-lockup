

void setup() {
  // put your setup code here, to run once:
  // 8,10 돌아가고,
  // 9,11 반대로
  Serial.begin(9600);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(8,HIGH);
  digitalWrite(10,HIGH);
    digitalWrite(9,LOW);
  digitalWrite(11,LOW);
  delay(5000);
  digitalWrite(8,LOW);
  digitalWrite(10,LOW);

  delay(5000);

    digitalWrite(9,HIGH);
  digitalWrite(11,HIGH);
    digitalWrite(8,LOW);
  digitalWrite(10,LOW);
  delay(5000);
  digitalWrite(9,LOW);
  digitalWrite(11,LOW);

  delay(5000);
}