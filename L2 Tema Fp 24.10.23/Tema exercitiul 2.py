
def cif(nr1, nr2):

    if nr1 % 10 == (nr2 // 10) % 10 and nr2 % 10 == (nr1 // 10) % 10:
        return True

    return False

def lista(vect):
    ct = 0

    for i in range(len(vect) - 1):

        for j in range(i + 1, len(vect), 1):

            if (cif(vect[i], vect[j])) == True:
                ct += 1

    return ct

def main():

    print(lista([96,69,47,23,32]))

main()