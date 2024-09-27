def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Fahrenheit to Celsius')
    print('4. Celsius to Fahrenheit')

def km_miles():
    km = float((input('Please enter distance in Kilometers: ')))
    miles = km / 1.60934
    print('Distance in miles {0}'.format(miles))

def miles_km():
    miles = float((input('Please enter distance in Miles: ')))
    km = miles * 1.60934
    print('Distance in Kilometers {0}'.format(km))

def celsius_to_fahrenheit():
    C = float(input('Please enter the Tempature value in Celsius: '))
    F = C * (9 / 5) + 32
    print('Tempature in Farenheit: {0}.format(F)')
    
def fahrenheit_to_celsius():
    F = float(input('Please enter the Tempature value in Farenheit: '))
    C = (F + 32) * (9 / 5)
    print('Tempature in Celsius: {0}.format(C)')

if __name__ == '__main__':
    print_menu()
    choice = input('Which would you like to do today?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
    if choice == '3':
        celsius_to_fahrenheit()
    if choice =='4':
        fahrenheit_to_celsius()