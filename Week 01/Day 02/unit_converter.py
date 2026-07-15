#================= Unit Converter Program......  ====================


def km_to_m(km):
    return km * 1000

def m_to_km(m):
    return m / 1000

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kg_to_g(kg):
    return kg * 1000

def g_to_kg(g):
    return g / 1000


while True:
    print("\n===== UNIT CONVERTER =====")
    print("1. Kilometer to Meter")
    print("2. Meter to Kilometer")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilogram to Gram")
    print("6. Gram to Kilogram")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        km = float(input("Enter kilometers: "))
        print("Meters =", km_to_m(km))

    elif choice == 2:
        m = float(input("Enter meters: "))
        print("Kilometers =", m_to_km(m))

    elif choice == 3:
        c = float(input("Enter temperature in Celsius: "))
        print("Fahrenheit =", celsius_to_fahrenheit(c))

    elif choice == 4:
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Celsius =", fahrenheit_to_celsius(f))

    elif choice == 5:
        kg = float(input("Enter kilograms: "))
        print("Grams =", kg_to_g(kg))

    elif choice == 6:
        g = float(input("Enter grams: "))
        print("Kilograms =", g_to_kg(g))

    elif choice == 7:
        print("Thank you for using Unit Converter!")
        break

    else:
        print("Invalid Choice! Please try again.")
    print("\n========================================")
