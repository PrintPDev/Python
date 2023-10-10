'''

Bisher hatten wir immer Funktionen die nur von Objekten, also Instanzen von Klassen, 
aufgerufen werden können. Allerdings gibt es auch Funktionen die auch von der Klasse selbst 
aufgerufen werden können. Das sind "Statische"-Funktionen und sind für Logik gedacht die
Allgemein sind und nicht von Eigenschaften eines spezifischen Objekts abhängig sind.

Beispiel: Eine Veranstaltung besteht aus Teilnehmer (Personen). Jedes erzeugte Objekte ist ein
neuer Teilnehmer in der Veranstaltung. Wie können wir die Anzahl der Teilnehmer speichern?#

-> Statische Funktion mit einem privaten Klassen-Attribut.

'''

class Person:
    __name = None
    __alter = None
    # Zählt die Instanzen der Objekte
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


def main():
    print(Person.teilnehmer_anzahl())
    p1 = Person('Saif', 27)
    print(Person.teilnehmer_anzahl())
    p2 = Person('Jan', 25)
    print(Person.teilnehmer_anzahl())
    p3 = Person('John', 30)
    print(p3.teilnehmer_anzahl())
    print(Person.teilnehmer_anzahl())


if __name__ == "__main__":
    main()
