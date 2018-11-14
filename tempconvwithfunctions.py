def is_ctof_or_ftoc() -> bool:
    
    is_celcius_to_fahrenheit: bool

    print("Choose one of the following:\n1: Celcius to Fahrenheit\n2: Fahrenheit to Celcius")
    tempurature_type = input()

    if tempurature_type == "1":
    
        is_celcius_to_fahrenheit = True

    elif tempurature_type == "2":
    
        is_celcius_to_fahrenheit = False

    else:
    
        print("Invalid entry, please try again")
        is_celcius_to_fahrenheit = is_ctof_or_ftoc()

    return is_celcius_to_fahrenheit


def get_temperature(is_celcius_to_fahrenheit: bool) -> float:

    temperature: float

    if is_celcius_to_fahrenheit == True:
        
        print("Please enter the tempurature in Celcius: ")

    elif is_celcius_to_fahrenheit == False:
 
        print("Please enter the tempurature in Fahrenheit: ")
    
    temperature = float(input())

    return temperature

def convert_celcius_to_fahrenheit(temperature: float) -> float:

    temperature = ((temperature *9) / 5) + 32
    print(f"The temperature in Fahrenheit is {temperature} degrees")

    return temperature

def convert_fahrenheit_to_celcius(temperature: float) -> float:

    temperature = ((temperature - 32) * 5) / 9
    print(f"The temperature in Celcius is {temperature} degrees")

    return temperature

temperature: float
is_celcius_to_fahrenheit: bool

is_celcius_to_fahrenheit = is_ctof_or_ftoc()

temperature = get_temperature(is_celcius_to_fahrenheit)

if is_celcius_to_fahrenheit == True:

    convert_celcius_to_fahrenheit(temperature)

elif is_celcius_to_fahrenheit == False:

    convert_fahrenheit_to_celcius(temperature)
