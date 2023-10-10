'''

Bisher haben wir Attribute NACH der Erzeugung von Objekten definiert. Das macht
aber nicht immer Sinn, wenn Objekte ohne Attribute erstellt werden. 

Beispiel: Eine Person hat immer einen Namen und deshalb macht es keinen Sinn
eines ohne dieses Attribut zu erstellen. 

Wie erzwingen wir das?

'''

class Person:
    name = None
    alter = None

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def daten_ausgeben(self):
        print('Mein Name ist: ', self.name)
        print('Mein Alter ist: ', self.alter)

    def daten_aendern(self, name, alter):
        self.name = name
        self.alter = alter


def main():
    # p1 = Person() So zuerst, da dann gezeigt wird, dass die KLasse fehler auswirft.
    p1 = Person('Saif', 27)
    p1.name = 'Saif'
    p1.alter = 27
    p1.daten_ausgeben()
    p1.daten_aendern('Jan', 25)
    p1.daten_ausgeben()


if __name__ == "__main__":
    main()
