def ask_for_numbers():
    a = input('Bitte gib die erste Zahl ein: ')
    b = input('Bitte gib die zweite Zahl ein: ')
    return a, b

def add(a, b):
    z = float(a) + float(b)
    return z

def subtract(a, b):
    z = float(a) - float(b)
    return z
    
def multiply(a, b):
    z = float(a) * float(b)
    return z

def divide(a, b):
    z = float(a) / float(b)
    return z

def check_option(option):
    if option.isdigit():
        if int(option) in [1,2,3,4,0]:
            return True
    return False

def print_menu():
    option = ''

    while check_option(option) is False:
        print('Bitte wähle einer der folgenden Optionen aus:')
        print(' 1 - Addieren von zwei Zahlen')
        print(' 2 - Subtrahieren von zwei Zahlen')
        print(' 3 - Multiplizieren von zwei Zahlen')
        print(' 4 - Dividieren von zwei Zahlen')
        print(' 0 - Abbrechen')
        print()
        option = input('Deine Wahl: ')
    
    option = int(option)
    
    return option

def start_dialog():
    option = print_menu()
    z = None

    if option == 0:
        exit(1)
    elif option == 1:
        a, b = ask_for_numbers()
        z = add(a, b)
    elif option == 2:
        a, b = ask_for_numbers()
        z = subtract(a, b)
    elif option == 3:
        a, b = ask_for_numbers()
        z = multiply(a, b)
    elif option == 4:
        a, b = ask_for_numbers()
        z = divide(a, b)
    else:
        print("Bitte die Eingabe wiederholen")

    print()
    print('Das Ergebnis ist: ', z)
    print()
    start_dialog()

def main():
    print('Willkommen beim Rechner!')
    start_dialog()

if __name__ == "__main__":
    main()