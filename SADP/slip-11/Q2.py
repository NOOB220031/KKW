# Program to interface LED to Raspberrry Pi  
import RPi.GPIO as GPIO  
import time  

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(8,GPIO.OUT)  
GPIO.setup(10,GPIO.OUT)  
GPIO.setup(16,GPIO.OUT)  
GPIO.setup(18,GPIO.OUT)  
GPIO.setup(22,GPIO.OUT)  
GPIO.setup(24,GPIO.OUT)  
GPIO.setup(26,GPIO.OUT)  
GPIO.setup(32,GPIO.OUT)  
GPIO.output(8,False)  
GPIO.output(10,False)  
GPIO.output(16,False)  
GPIO.output(18,False)  
GPIO.output(22,False)  
GPIO.output(24,False)  
GPIO.output(26,False)  
GPIO.output(32,False)  

while(True):  
    GPIO.output(8,True)  
    GPIO.output(10,True)  
    GPIO.output(16,True)  
    GPIO.output(18,True)  
    GPIO.output(22,True)  
    GPIO.output(24,True)  
    GPIO.output(26,True)  
    GPIO.output(32,True)  
    print("LED ON")  
    time.sleep(2)  
    GPIO.output(8,False)  
    GPIO.output(10,False)  
    GPIO.output(16,False)  
    GPIO.output(18,False)  
    GPIO.output(22,False)  
    GPIO.output(24,False)  
    GPIO.output(26,False)  
    GPIO.output(32,False)  
    print("LED OFF")  
    time.sleep(2)  

# Program 2  
# Program to interface LED to Raspberry Pi  

import RPi.GPIO as GPIO  
import time  

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(8,GPIO.OUT)  
GPIO.setup(10,GPIO.OUT)  
GPIO.setup(16,GPIO.OUT)  
GPIO.setup(18,GPIO.OUT)  
GPIO.setup(22,GPIO.OUT)  
GPIO.setup(24,GPIO.OUT)  
GPIO.setup(26,GPIO.OUT)  
GPIO.setup(32,GPIO.OUT)  
GPIO.output(8,False)  
GPIO.output(10,False)  
GPIO.output(16,False)  
GPIO.output(18,False)  
GPIO.output(22,False)  
GPIO.output(24,False)  
GPIO.output(26,False)  
GPIO.output(32,False)  

while(True):  
    GPIO.output(8,True)  
    time.sleep(0.2)  
    GPIO.output(10,True)  
    time.sleep(0.2)  
    GPIO.output(16,True)  
    time.sleep(0.2)  
    GPIO.output(18,True)  
    time.sleep(0.2)  
    GPIO.output(22,True)  
    time.sleep(0.2)  
    GPIO.output(24,True)  
    time.sleep(0.2)  
    GPIO.output(26,True)  
    time.sleep(0.2)  
    GPIO.output(32,True)  
    time.sleep(0.2)  
    GPIO.output(8,False)  
    time.sleep(0.2)  
    GPIO.output(10,False)  
    time.sleep(0.2)  
    GPIO.output(16,False)  
    time.sleep(0.2)  
    GPIO.output(18,False)  
    time.sleep(0.2)  
    GPIO.output(22,False)  
    time.sleep(0.2)  
    GPIO.output(24,False)  
    time.sleep(0.2)  
    GPIO.output(26,False)  
    time.sleep(0.2)  
    GPIO.output(32,False)  
    time.sleep(0.2)  

# Program 3  
# Progrtam to take feedback from the switch using Raspberry Pi  

import RPi.GPIO as GPIO  
import time  

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(8,GPIO.IN)  
GPIO.setup(10,GPIO.OUT)  
GPIO.output(10,False)  
y=0  
dcount=0  
while(True):  
    x = GPIO.input(8)  
#single pressed  
    if(x==0):  
        GPIO.output(10,True)  
        print("Switch Pressed")  
    else:  
        GPIO.output(10,False)  
        print("Switch Released")