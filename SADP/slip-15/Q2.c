int vibrationSensorPin = A0; 
int  counter;          // count n samples  
int newValue; 
int minValue; 
int maxValue; 

void setup()  {  
    Serial.begin(115200);  
    counter = 0;                  // start at the begin  
    minValue = analogRead(vibrationSensorPin);    
    maxValue = analogRead(vibrationSensorPin); 
    // give them a value from the sensor to start with 

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
            Serial.println("finger Detected");     
        else  
            Serial.println("finger NOT deteced");  
        
            counter = 0;                // start at the begin  
        minValue = analogRead(vibrationSensorPin);     
        maxValue = analogRead(vibrationSensorPin); // give them a value from the sensor to start with  
    }  
    delay( 20);        
}