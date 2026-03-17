#conversion of temperature from celsius to fahrenheit and vice versa
#To convert temperature from celsius to fahrenheit we can use the formula F = (C * 9/5) + 32
temp_celsius = float(input("Enter temperature in Celsius: "))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print("Temperature in Fahrenheit: ", temp_fahrenheit)

#To convert temperature from fahrenheit to celsius we can use the formula C = (F - 32) * 5/9
temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
temp_celsius = (temp_fahrenheit - 32) * 5/9
print("Temperature in Celsius: ", temp_celsius)