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

    def __init__(self, name, alter):
        self.__name = name
        self.__alter = alter

    def daten_ausgeben(self):
        print('Mein Name ist: ', self.__name)
        print('Mein Alter ist: ', self.__alter)

    def daten_aendern(self, name, alter):
        self.__name = name
        self.__alter = alter


def main():
    p1 = Person('Saif', 27)
    p1.__name = 'Saif'
    p1.__alter = 27
    p1.daten_ausgeben()
    p1.daten_aendern('Jan', 25)
    p1.daten_ausgeben()


if __name__ == "__main__":
    main()
