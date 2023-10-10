class Student():
    pass

class Veranstaltung():
    pass
    

class VeranstaltungManagement():

    def check_option(self, option):
        if option.isdigit():
            if int(option) in [1,2,3,4,0]:
                return True
        return False

    def print_menu(self):
        option = ''

        while self.check_option(option) is False:
            print('Bitte wähle einer der folgenden Optionen aus:')
            print(' 1 - Alle Veranstaltungen anzeigen')
            print(' 2 - Veranstaltung hinzufügen')
            print(' 3 - Veranstaltung löschen')
            print(' 4 - Studierende einer Veranstaltung hinzufügen')
            print(' 0 - Programm beenden')
            print()
            option = input('Deine Wahl: ')
        
        option = int(option)
        
        return option

    def start_dialog(self):
        option = self.print_menu()

        if option == 0:
            exit(1)
        elif option == 1:
            self.veranstaltungen_ausgeben()
        elif option == 2:
            self.veranstaltung_hinzufuegen()
        elif option == 3:
            self.veranstaltung_entfernen()
        elif option == 4:
            self.studierende_hinzufuegen()
        else:
            print("Bitte die Eingabe wiederholen")
        
        self.start_dialog()

    def veranstaltung_hinzufuegen(self):
        pass

    def veranstaltung_entfernen(self):
        pass
    
    def veranstaltungen_ausgeben(self):
        pass

    def studierende_hinzufuegen(self):
        pass


def main():
    print('Willkommen bei der Veranstaltugsanmeldung!')
    veranstaltungen = VeranstaltungManagement()
    veranstaltungen.start_dialog()

if __name__ == "__main__":
    main()