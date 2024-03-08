#include <DHT.h>

// Define DHT sensor type and pins
#define DHTTYPE DHT22
#define DHTPIN1 4   // Example GPIO pins, change as needed
#define DHTPIN2 5
#define DHTPIN3 18
#define DHTPIN4 19
#define CO2_SENSOR_PIN 34 // Assuming an analog CO2 sensor

DHT dht1(DHTPIN1, DHTTYPE);
DHT dht2(DHTPIN2, DHTTYPE);
DHT dht3(DHTPIN3, DHTTYPE);
DHT dht4(DHTPIN4, DHTTYPE);

void setup() {
  Serial.begin(115200); // Start serial communication with the Pi at 115200 baud rate
  dht1.begin();
  dht2.begin();
  dht3.begin();
  dht4.begin();
}

void loop() {
  // Read temperature and humidity from each DHT sensor
  float temp1 = dht1.readTemperature();
  float hum1 = dht1.readHumidity();
  float temp2 = dht2.readTemperature();
  float hum2 = dht2.readHumidity();
  float temp3 = dht3.readTemperature();
  float hum3 = dht3.readHumidity();
  float temp4 = dht4.readTemperature();
  float hum4 = dht4.readHumidity();
  
  // Read CO2 sensor (analog)
  int co2Value = analogRead(CO2_SENSOR_PIN);

  // Format the data into a single string
  String data = String(temp1) + "," + String(hum1) + "," +
                String(temp2) + "," + String(hum2) + "," +
                String(temp3) + "," + String(hum3) + "," +
                String(temp4) + "," + String(hum4) + "," +
                String(co2Value);

  // Send the data to Raspberry Pi via UART
  Serial.println(data);

  // Wait for a minute before the next read
  delay(60000);
}
