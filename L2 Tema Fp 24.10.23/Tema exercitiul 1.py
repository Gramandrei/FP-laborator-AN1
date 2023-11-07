
def rep(vect):

    nou_vect = []

    for i in range(len(vect) - 1):

        if vect[i] not in nou_vect:

            nou_vect.append(vect[i])

    return nou_vect

def main():

    print(rep([11,22,22,24,24,26,27]))


main()


