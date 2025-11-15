#include <DHT.h>  
/*  Interfacing Temperature and Humidity Sensor (DHT11)-using One Wire 
Protocol */  
#include<DHT.h>                    
#define DHTTYPE DHT11          
int dhtSensorPin = 6;  
//define library for sensor  
//define macro  
DHT dht(dhtSensorPin, DHTTYPE);      
//pin initialization 
float t, h;  

void setup()  {  
    Serial.begin(9600);  
    dht.begin();   
    pinMode(dhtSensorPin, INPUT);  
    delay(2000);  
}  
void loop() { 
    t = dht.readTemperature();  //object to read the sensor value 
    Serial.print("Temperature="); 
    Serial.println(t); 
    
    h = dht.readHumidity(); 
    Serial.print("Humidity="); 
    Serial.println(h); 
    
    delay(500); 
}