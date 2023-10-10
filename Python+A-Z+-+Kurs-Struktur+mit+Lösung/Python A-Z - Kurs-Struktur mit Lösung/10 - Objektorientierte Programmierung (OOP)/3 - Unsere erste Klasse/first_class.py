'''

Wir haben gesagt das in Python alles eine Klasse ist. 

Wie können wir nun eine eigene Klasse erstellen?

'''


# Lass uns eine Klasse definieren die "Person" heißt

class Person: # Name der Klasse singular nicht plural (Person: +; Stühle: -)
    pass


def main():
    p1 = Person()
    p2 = Person()

    p3 = p1

    print('Ist p3 = p1? ', (p3 == p1))
    print('Ist p1 = p2? ', (p1 == p2))

if __name__ == "__main__":
    main()
