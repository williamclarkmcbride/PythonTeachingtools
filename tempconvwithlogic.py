temperature: float
tempurature_type: str
is_celcius_to_fahrenheit: bool

print("Choose one of the following:\n1: Celcius to Fahrenheit\n2: Fahrenheit to Celcius")
tempurature_type = input()

if tempurature_type == "1":
    
    is_celcius_to_fahrenheit = True
    print("Please enter the tempurature in Celcius: ")

elif tempurature_type == "2":
    
    is_celcius_to_fahrenheit = False
    print("Please enter the tempurature in Fahrenheit: ")

else:
    
    print("Invalid entry, please start over")
    quit()

temperature = float(input())

if is_celcius_to_fahrenheit == True:
    
    temperature = ((temperature *9) / 5) + 32
    print(f"The temperature in Fahrenheit is {temperature} degrees")

elif is_celcius_to_fahrenheit == False:
    
    temperature = ((temperature - 32) * 5) / 9
    print(f"The temperature in Celcius is {temperature} degrees")
