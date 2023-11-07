from math import gcd
def simplify(a):
    d = gcd(a[0], a[1])

    return (a[0] // d, a[1]//d)

def test_simplify():
    assert simplify((4,4))==(1,1)


def add(a, b):
    return simplify((a[0] * b[1] + a[1] * b[0], a[1] * b[1]))

def test_add():
    assert add((1, 2), (2, 3)) == (7, 6)
    assert add((1, 2), (1, 2)) == (1, 1)

def sub():
    return a[1] * b[0] - a[0] * b[1], a[1] * b[1]

def test_sub(a, b):
    assert sub((1, 2), (2, 3)) == (-1, 6)

def menu():
    return """
    1 - add frac
    2 - sum fracs
    3 - sub fracs
    0 - exit
    """

def main():
    fracs=[]

    while True:
        print (menu())

        opt = int(input('opt = '))

        if opt == 1:
            n = int(input('n = '))
            m = int(input('m = '))
            add_frac(fracs, (n, m))

        if opt == 2:
            s =sum_frac(fracs)
            print(s)

        if opt == 3:
            b= sub
            print(b)

        if opt == 0:
            break



def add_frac(fracs, frac):
    fracs.append(frac)


def sum_frac(fracs):
    sum = 0, 1

    for frac in fracs:
        sum = add(sum, frac)

    return simplify(sum)

def test_sum_frac():
    assert sum_frac([ (1, 2), (2, 3), (1, 2)]) == (5, 3)
    assert add((1, 2), (1, 2)) == (1, 1)


test_sum_frac()
test_add()

test_simplify()
main()