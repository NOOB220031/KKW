# print_name_n_times.py  
name = input("Enter your name: ")  
n = int(input("How many times to print your name? "))  

print("\nUsing for loop:")  

for i in range(n):  
    print(f"{i+1}: {name}")  

print("\nUsing while loop:")  
count = 0  

while count < n:  
    print(f"{count+1}: {name}")  
    count += 1  

# divide_exception.py  
try:  
    num1 = float(input("Enter numerator: "))  
    num2 = float(input("Enter denominator: "))  
    result = num1 / num2  
    print(f"Result = {result}")  
except ZeroDivisionError:  
    print("Error: Division by zero is not allowed.")  

# print_time_interval.py  

import time  
from datetime import datetime  

print("Printing current time every 10 seconds (10 times):")  
for i in range(10):  
    print(f"{i+1}: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")  
    time.sleep(10)  

# file_word_count.py  

file_path = input("Enter file path (e.g., /home/pi/test.txt): ")  
try:  
    with open(file_path, 'r') as f:  
        line_num = 1  
    
    for line in f:  
        words = line.strip().split()  
        print(f"Line {line_num}: {len(words)} words")  
        line_num += 1  
except FileNotFoundError:  
    print("File not found. Please check the path.") 