'''
Jedes Python-Modul bietet viele Funktionen und Eigenschaften an die du
mit der dir()-Funktion ausgeben lassen kannst.


'''


import math
import random


def main():
    inhalt_math = dir(math)
    print('Funktionen und Eigenschaften von math: \n', inhalt_math)

    inhalt_random = dir(random)
    print('Funktionen und Eigenschaften von random: \n', inhalt_random)

    '''
        Die Dokumentation der einzelnen Module findet ihr auf folgender 
        Seite: https://docs.python.org/3/py-modindex.html
    '''

if __name__ == "__main__":
    main()