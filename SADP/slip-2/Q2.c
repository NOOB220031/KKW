int trigPin = D4;
int echoPin = D8;
void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}
void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  int duration =    pulseIn(echoPin, HIGH);
  
  int distance = duration * 0.034 / 2;
  
  Serial.print("Distance in cm is: ");
  Serial.println(distance);
  delay(100);
}
