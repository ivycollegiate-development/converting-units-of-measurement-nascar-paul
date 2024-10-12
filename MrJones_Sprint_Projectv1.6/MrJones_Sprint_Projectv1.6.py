import random

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Fahrenheit to Celsius')
    print('4. Celsius to Fahrenheit')

def km_miles():
    km = float((input('Please enter distance in Kilometers: ')))
    miles = km / 1.60934
    print('Distance in miles {0}'.format(miles))
    #Display a random distance fun fact, run the following
    print("Fun fact: ", random.choice(tempature_facts))

def miles_km():
    miles = float((input('Please enter distance in Miles: ')))
    km = miles * 1.60934
    print('Distance in Kilometers {0}'.format(km))

def celsius_to_fahrenheit():
    C = float(input('Please enter the Tempature value in Celsius: '))
    F = C * (9 / 5) + 32
    print('Tempature in Farenheit: {0}'.format(F))
    
def fahrenheit_to_celsius():
    F = float(input('Please enter the Tempature value in Farenheit: '))
    C = (F - 32) * (9 / 5)
    print('Tempature in Celsius: {0}'.format(C))

tempature_facts = [
"Earth's core is 9,392 °F.",
"212 °F is the boiling point of water.",
"The highest recorded temperature on Earth was in Death Valley, California where it reached 134 °F in 1913."
]

distance_facts = [
"The longest recorded flight of a chicken was 13 seconds.",
"The longest street in the world is Yonge street in Toronto Canada measuring 1,896 km (1,178 miles)!",
"Cats can jump up to 7 times their tail length."
]

if __name__ == '__main__':
    while True:
        print_menu()
        choice = input('Which would you like to do today?(Press q to quit): ')
        if choice == 'q':
            break
        if choice == '1':
            km_miles()
        if choice == '2':
            miles_km()
        if choice == '3':
            celsius_to_fahrenheit()
        if choice =='4':
            fahrenheit_to_celsius()