
def domino(nr1, nr2):

    if nr1 % 10 == (nr2 // 10) % 10:
        return True

    return False

def d_vect(vect):
    lg = 1
    l_max = 1

    for i in range(len(vect) - 1):

        if domino(vect[i], vect[i + 1]) == True:
            lg += 1

        else:
            lg = 1

        if lg > l_max:
            l_max = lg

    return l_max
def main():
    print(d_vect([89, 95, 54, 10, 12, 24, 42, 26, 67]))

main()