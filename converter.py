def convert(value, from_unit, to_unit):
    factors = {
        "meters": {"feet": 3.28084},
        "feet": {"meters": 1 / 3.28084},
        "kg": {"lbs": 2.20462},
        "lbs": {"kg": 1 / 2.20462},
        "Celsius": {"Fahrenheit": lambda x: (x * 9/5) + 32},
        "Fahrenheit": {"Celsius": lambda x: (x - 32) * 5/9}
    }
    
    if from_unit in factors and to_unit in factors[from_unit]:
        factor = factors[from_unit][to_unit]
        return factor(value) if callable(factor) else value * factor
    return None


def get_valid_unit(prompt, valid_units):
    while True:
        unit = input(prompt).strip().lower()
        if unit in valid_units:
            return unit
        print(f"Invalid unit! Please choose from: {', '.join(valid_units)}")


def main():
    print("Welcome to the Unit Converter!")
    print("1. Length (Meters <-> Feet)")
    print("2. Weight (Kilograms <-> Pounds)")
    print("3. Temperature (Celsius <-> Fahrenheit)")
    
    while True:
        choice = input("Choose a category (1/2/3): ")
        if choice in ["1", "2", "3"]:
            break
        print("Invalid choice! Please choose 1, 2, or 3.")
        
    value = float(input("Enter the value to convert: "))
    
    if choice == "1":
        valid_units = ["meters", "feet"]
        from_unit = get_valid_unit("Convert from (meters/feet): ", valid_units)
        to_unit = "feet" if from_unit == "meters" else "meters"
    elif choice == "2":
        valid_units = ["kg", "lbs"]
        from_unit = get_valid_unit("Convert from (kg/lbs): ", valid_units)
        to_unit = "lbs" if from_unit == "kg" else "kg"
    elif choice == "3":
        valid_units = ["celsius", "fahrenheit"]
        from_unit = get_valid_unit("Convert from (Celsius/Fahrenheit): ", valid_units)
        to_unit = "Fahrenheit" if from_unit == "celsius" else "Celsius"
    else:
        print("Invalid choice.")
        return
    
    result = convert(value, from_unit, to_unit)
    if result is not None:
        print(f"{value} {from_unit} is {result:.2f} {to_unit}.")
    else:
        print("Invalid units for conversion.")


if __name__ == "__main__":
    main()