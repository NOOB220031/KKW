int vibrationSensorPin = A0; 
int  counter;          
int newValue; 
int minValue; 
int maxValue; 

void setup()  {  
    Serial.begin(115200);  
    counter = 0;         
    minValue = analogRead(vibrationSensorPin);    
    maxValue = analogRead(vibrationSensorPin); 

}  

void loop()   {  
    newValue = analogRead(vibrationSensorPin);   
    
    if ( newValue >= maxValue) {  
        maxValue = newValue;  
    } else {  
        minValue = newValue;
        counter++;  
        if ( counter == 50) {  
            Serial.print(minValue);  
            Serial.print("  ");  
            Serial.print(maxValue);  
            Serial.print("  ");  
        }  
        
        if ((maxValue - minValue) > 250)       
            Serial.println("Vibration Detected");     
        else  
            Serial.println("Vibration NOT deteced");  
        
            counter = 0;                
        minValue = analogRead(vibrationSensorPin);     
        maxValue = analogRead(vibrationSensorPin);  
    }  
    delay( 20);        
}