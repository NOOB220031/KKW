
#define LDR_PIN A0     
#define LED_PIN D4     

void setup() {  
    Serial.begin(115200);      
    pinMode(LED_PIN, OUTPUT);   
}  

void loop() {   
    int ldrValue = analogRead(LDR_PIN); 
    Serial.print("LDR Value: ");  
    Serial.println(ldrValue);  


    int  threshold = 500;  

    if (ldrValue < threshold) {     
        digitalWrite(LED_PIN, LOW);  
    } else {  
        digitalWrite(LED_PIN, HIGH);   
    }  
    delay(500);   
} 