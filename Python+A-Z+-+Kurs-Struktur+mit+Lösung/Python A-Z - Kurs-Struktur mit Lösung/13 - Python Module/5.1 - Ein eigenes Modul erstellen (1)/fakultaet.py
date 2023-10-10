def iterative_fakultaet(n):
    result = 1
    for i in range(2, n+1):
        result *= i
        print(result)
    return result


def recursive_fakultaet(n):
    print('Rekursive Funktion aufgerufen für n = ' + str(n))
    if n == 0:
        return 1
    else:
        res = n * recursive_fakultaet(n - 1)
        print('Ergebnis für zwischenschritt: ', res)
        return res