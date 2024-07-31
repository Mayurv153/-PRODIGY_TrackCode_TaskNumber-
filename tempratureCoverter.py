def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    print("Welcome to the Temperature Conversion Program")
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if unit not in ['C', 'F', 'K']:
        print("Invalid unit. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")
        return

    target_unit = input("Enter the unit to convert to (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if target_unit not in ['C', 'F', 'K']:
        print("Invalid target unit. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")
        return

    if unit == 'C':
        if target_unit == 'F':
            converted_temp = celsius_to_fahrenheit(temp)
        elif target_unit == 'K':
            converted_temp = celsius_to_kelvin(temp)
        else:
            converted_temp = temp

    elif unit == 'F':
        if target_unit == 'C':
            converted_temp = fahrenheit_to_celsius(temp)
        elif target_unit == 'K':
            converted_temp = fahrenheit_to_kelvin(temp)
        else:
            converted_temp = temp

    elif unit == 'K':
        if target_unit == 'C':
            converted_temp = kelvin_to_celsius(temp)
        elif target_unit == 'F':
            converted_temp = kelvin_to_fahrenheit(temp)
        else:
            converted_temp = temp

    print(f"The converted temperature is {converted_temp} {target_unit}")

if __name__ == "__main__":
    convert_temperature()
