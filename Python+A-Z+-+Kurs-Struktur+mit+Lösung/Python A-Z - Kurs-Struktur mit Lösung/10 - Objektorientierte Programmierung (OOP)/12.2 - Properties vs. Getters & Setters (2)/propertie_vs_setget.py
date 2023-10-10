'''

Bisher konnten wir in der Person Klasse Attribute einfügen und diese direkt über das Objekt
ansprechen. Allerdings sollten wir nach dem Konzept der Datenkapslung diese Art vermeiden, richtig?

Die Antwort ist Jaein. Wir werden in dieser Lektion erst sehen wie wir Datenkapslung ähnlich zu den
Sprachen wie Java oder C/C++ realisieren können. Das werden wir tun ohne die Attribute direkt anzusprechen.

Wie? 

-> Wir erstellen setter und getter "Schnittstellen", also Funktionen, um die Attribute zu modifizieren.

Hinweis: Das ist leider nicht der Pythonic-Way wie man so etwas realisiert. Dazu mehr in der nächsten Lektion.
'''

class Person:
    __name = None
    __alter = None
    __teilnehmer = 0

    def __init__(self, name, alter):
        self.__name = name
        self.__alter = alter
        type(self).__teilnehmer += 1

    def daten_ausgeben(self):
        print('Mein Name ist: ', self.__name)
        print('Mein Alter ist: ', self.__alter)

    def daten_aendern(self, name, alter):
        self.__name = name
        self.__alter = alter
    
    @staticmethod
    def teilnehmer_anzahl():
        return Person.__teilnehmer

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_alter(self):
        return self.__alter

    def set_alter(self, alter):
        self.__alter = alter


def main():
    p1 = Person('Saif', 27)
    p1.daten_ausgeben()
    alter_p1 = p1.get_alter()
    p1.set_alter(alter_p1 + 5)
    p1.set_name('Dejan')
    p1.daten_ausgeben()


if __name__ == "__main__":
    main()
