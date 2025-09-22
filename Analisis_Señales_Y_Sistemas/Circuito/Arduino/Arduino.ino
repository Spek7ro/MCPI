int ledPin = 9;
int sensorPin = A0;
int value;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // LED parpadeando con 10 Hz (aprox)
  digitalWrite(ledPin, HIGH);
  delay(50);
  digitalWrite(ledPin, LOW);
  delay(50);

  // Lectura de señal analógica
  value = analogRead(sensorPin);
  Serial.println(value); // Enviar al monitor serial
}
