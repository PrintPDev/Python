'''

In der letzten Lektion haben wir Datenkapslung anhand von setter und getter "Schnittstellen"
umgesetzt. Allerdings ist das nicht der Pythonic-Way so etwas zu implementieren. 

Komischerweise ist es in Python üblich Attribute öffentlich zu setzen und Datenkapslung
über ein Decorater zu realisieren.

Wie? 

-> Wir erstellen Funktion worüber Python weiß, dass diese für das schreiben und lesen eines Attributes ist.


'''

class Person:
    alter = 0

    def __init__(self, alter):
        self.alter = alter

    def daten_ausgeben(self):
        print('Mein Alter ist: ', self.__alter)


def main():
    pass

if __name__ == "__main__":
    main()
