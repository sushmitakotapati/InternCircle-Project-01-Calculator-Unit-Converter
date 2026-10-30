
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def addition():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print("Result:", a + b)


def subtraction():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print("Result:", a - b)


def multiplication():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print("Result:", a * b)


def division():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    if b != 0:
        print("Result:", round(a / b, 2))
    else:
        print("Cannot divide by zero.")


def km_to_miles():
    km = get_number("Enter distance in kilometers: ")
    miles = km * 0.621371
    print("Miles:", round(miles, 2))


def celsius_to_fahrenheit():
    celsius = get_number("Enter temperature in Celsius: ")
    fahrenheit = (celsius * 9 / 5) + 32
    print("Fahrenheit:", round(fahrenheit, 2))


while True:
    print("\n--- Calculator & Unit Converter ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Kilometers to Miles")
    print("6. Celsius to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addition()
    elif choice == "2":
        subtraction()
    elif choice == "3":
        multiplication()
    elif choice == "4":
        division()
    elif choice == "5":
        km_to_miles()
    elif choice == "6":
        celsius_to_fahrenheit()
    elif choice == "7":
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid choice. Please try again.")
