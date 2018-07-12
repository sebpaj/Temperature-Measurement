float temp;
float temp2;

void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  temp = analogRead(A1);
  temp = temp * 0.48828125;
  temp2 = analogRead(A2);
  temp2 = temp2 * 0.48828125;
  Serial.print("First Sensor Temperature: ");
  Serial.print(temp);
  Serial.print("*C");
  Serial.println();
  Serial.print("Second Sensor Temperature: ");
  Serial.print(temp2);
  Serial.print("*C");
  Serial.println();
  delay(1000);
}
