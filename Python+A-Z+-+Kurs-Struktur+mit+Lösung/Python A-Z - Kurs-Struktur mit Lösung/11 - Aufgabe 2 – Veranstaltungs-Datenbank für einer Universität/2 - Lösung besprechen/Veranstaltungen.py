class Student():
    name = None

    def __init__(self):
        self.name = input('Bitte gebe den Namen des Studenten ein: ')

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if type(name) != str or name.isdigit():
            raise TypeError('Für name sind nur folgende Zeichen gültig: A-Z und a-z')
        self.__name = name

class Veranstaltung():
    titel = None
    studierende = None

    def __init__(self):
        name = input('Bitte gebe den Titel der Veranstaltung ein: ')
        self.titel = name
        self.studierende = []

    @property
    def titel(self):
        return self.__titel

    @titel.setter
    def titel(self, titel):        
        if type(titel) != str:
            raise TypeError('Für Titel sind nur folgende Zeichen gültig: A-Za-z und 0-9')
        self.__titel = titel

    @property
    def teilnehmeranzahl(self):
        return len(self.studierende)

    def student_hinzufuegen(self, student):
        if isinstance(student, Student) is False:
            raise TypeError('student scheint nicht von der Student-Klasse zu stammen.')
        self.studierende.append(student)
    
    def start_dialog(self):
        while True:
            std_hinzufuegen = input('Möchten Sie Studierende hinzufuegen? (j/n)\n')
            if std_hinzufuegen == 'j':
                st = Student()
                self.student_hinzufuegen(st)
            else:
                break
    

class VeranstaltungManagement():
    veranstaltungen = None

    def __init__(self):
        self.veranstaltungen = []

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
        v = Veranstaltung()
        v.start_dialog()
        self.veranstaltungen.append(v)

    def veranstaltung_entfernen(self):
        self.veranstaltungen_ausgeben()

        while True:
            v_nr = input('Bitte geben Sie zum löschen die Veranstaltungsnummer: ')
            
            if v_nr.isdigit() == False:
                print('Bitte geben Sie eine Veranstaltungsnummer ein!')
            else:
                v_nr = int(v_nr)
                if v_nr >= len(self.veranstaltungen):
                    print('Bitte gebe eine gültige Nummer ein!')
                else:
                    self.veranstaltungen.pop(v_nr)
                    print('Veranstaltung gelöscht...')
                    break
    
    def veranstaltungen_ausgeben(self):
        if len(self.veranstaltungen) == 0:
            print('Es existieren noch keine Veranstaltungen.. Bitte trage neue ein.')
            print()
        else:
            print('Folgende Veranstaltungen sind gespeichert: ')
            for i, v in enumerate(self.veranstaltungen):
                print('Veranstaltungsnummer: ', i)
                print('Titel: ', v.titel)
                print('Teilnehmeranzahl: ', v.teilnehmeranzahl)
                print()

    def studierende_hinzufuegen(self):
        self.veranstaltungen_ausgeben()

        while True:
            v_nr = input('Bitte geben Sie die Veranstaltungsnummer ein: ')
            
            if v_nr.isdigit() == False:
                print('Bitte geben Sie eine gültige Veranstaltungsnummer ein!')
            else:
                v_nr = int(v_nr)
                if v_nr >= len(self.veranstaltungen):
                    print('Bitte gebe eine gültige Nummer ein!')
                else:
                    v = self.veranstaltungen.pop(v_nr)
                    v.start_dialog()
                    self.veranstaltungen.append(v)
                    break


def main():
    print('Willkommen bei der Veranstaltugsanmeldung!')
    veranstaltungen = VeranstaltungManagement()
    veranstaltungen.start_dialog()

if __name__ == "__main__":
    main()