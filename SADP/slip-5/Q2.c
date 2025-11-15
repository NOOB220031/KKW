#include <ESP8266WiFi.h>  
// Replace with your actual Wi-Fi credentials 
const char* ssid = "RedmiNote8Pro";        
// Enter your Wi-Fi name (SSID) 
const char* password =  "12345678"; //    Enter your Wi-Fi password  

void setup() {    
    Serial.begin(115200);    
    delay(100);        
    // Start Wi-Fi  Connection  
    Serial.println();  
    Serial.println("Connecting to WiFi...");  
    WiFi.begin(ssid, password);  // Connect to WiFi    // Wait until connected  
    
    while (WiFi.status() != WL_CONNECTED) {     
        delay(500);  
        Serial.print(".");  
    }  
    
    Serial.println();  
    Serial.println("WiFi connected!");  
    Serial.print("IP Address: ");  
    Serial.println(WiFi.localIP());  
}  

void loop() {  
    // You can add tasks here that require WiFi connection 
} 