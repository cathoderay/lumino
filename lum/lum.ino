
int a = 0;
int b = 5;

void setup() {
  Serial.begin(9600);
  pinMode(a, INPUT);
  pinMode(b, INPUT);
}

void loop() {
  Serial.print(analogRead(a));
  Serial.print(" ");
  Serial.print(analogRead(b));
  delay(10);
}
