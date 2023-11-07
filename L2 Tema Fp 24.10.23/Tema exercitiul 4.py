


def criptare(vect):

    c = vect[0]

    for i in range(1, len(vect)):

        vect[i] = c * vect[i]

    return vect

def main():
    print(criptare([12, 15, 13]))

main()