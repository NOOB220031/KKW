# hello_name.py  

name = input("Enter your name: ") 
print(f"Hello, {name}! Welcome to Raspberry Pi.")  

# basic_math.py 

a = float(input("Enter first number: "))  
b = float(input("Enter second number: "))  

print(f"Sum = {a + b}") 
print(f"Difference = {a - b}") 
print(f"Product = {a * b}") 
if b != 0:  
    print(f"Division = {a / b}") 
else:  
    print("Division by zero is not allowed.")  

# count_words_chars.py  

text = input("Enter a string: ")  
words = text.split() 
num_words = len(words)  
num_chars = len(text)  

print(f"Word count: {num_words}") 
print(f"Character count (including spaces): {num_chars}") 

# area_calculator.py  

import math  
shape = input("Enter shape (rectangle/triangle/circle): ").lower()   
  
if shape == "rectangle":  
    length = float(input("Enter length: "))     
    breadth = float(input("Enter breadth: "))     
    area = length * breadth  
    print(f"Area of rectangle = {area:.2f}")  
elif shape == "triangle":  
    base = float(input("Enter base: "))     
    height = float(input("Enter height: "))     
    area = 0.5 * base * height  
    print(f"Area of triangle = {area:.2f}")  
elif shape == "circle":  
    radius = float(input("Enter radius: "))     
    area = math.pi * radius ** 2  
    print(f"Area of circle = {area:.2f}")  
else:     
    print("Invalid shape entered.")