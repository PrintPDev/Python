'''

Wir haben nun gesehen wie wir einen Fehler abfangen können. Allerdings 
gibt es Fälle wo gewisse Logik-Abschnitte mehrere Fehler auslösen können.

Lass uns einen Fall durchgehen!

'''


def main():
    try:
        f = open('integers.txt')
        s = f.readline()
        i = int(s.strip())
        print(i)
    except IOError as e:
        print('I/O Fehler: ', e)
    except ValueError:
        print("Keine Zahl in dieser Zeile")
    except:
        print("Unerwarteter Fehler:")
        raise

if __name__ == "__main__":
    main()