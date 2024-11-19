'''map my work:
write a program that converts fahrenheit and celsius
using user input'''

#asks user for celcius input
celcius = int(input("Enter the temperature in Celcius:"))

#do calculations to convert 
results = (celcius * (9/5) + 32)

#print results to terminal 
print("The temperature is", results, "degrees Fahrenheit")