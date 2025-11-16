#include <ESP8266WiFi.h>  

const char* ssid = "RedmiNote8Pro";         
const char* password =  "12345678";

void setup() {    
    Serial.begin(115200);    
    delay(100);        
    
    Serial.println();  
    Serial.println("Connecting to WiFi...");  
    WiFi.begin(ssid, password);
    
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
} 