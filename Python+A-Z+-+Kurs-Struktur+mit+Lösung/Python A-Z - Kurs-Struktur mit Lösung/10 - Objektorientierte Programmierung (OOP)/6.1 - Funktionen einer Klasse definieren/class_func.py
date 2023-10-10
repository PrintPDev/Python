'''

Klassen können natürlich, neben Attribute, auch Funktionen enthalten, um Logik 
spezifisch für die Klasse bereitzustellen.

'''

class Person: 
    name = None
    alter = None

    def daten_ausgeben(self):
        print('Mein Name ist: ', self.name)
        print('Mein Alter ist: ', self.alter)

    def daten_aendern(self, name, alter):
        self.name = name
        self.alter = alter


def main():
    p1 = Person()
    p1.name = 'Saif'
    p1.alter = 27
    p1.daten_ausgeben()
    p1.daten_aendern('Jan', 25)
    p1.daten_ausgeben()


if __name__ == "__main__":
    main()
