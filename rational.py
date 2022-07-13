from math import gcd


def make_rational(numer, denom):
    devisor = gcd(numer, denom)
    if devisor != 1:
        numer = numer / devisor
        denom = denom / devisor
    return {'numer': int(numer), 'denom': int(denom)}

def get_numer(rat):
    return rat['numer']

def get_denom(rat):
    return rat['denom']

def add(rat1, rat2):
    num1, num2 = get_numer(rat1), get_numer(rat2)
    den1, den2 = get_denom(rat1), get_denom(rat2)
    denom = den1 * den2
    numer = num1 * den2 + num2 * den1
    return make_rational(numer, denom)

def sub(rat1, rat2):
    num1, num2 = get_numer(rat1), get_numer(rat2)
    den1, den2 = get_denom(rat1), get_denom(rat2)
    denom = den1 * den2
    numer = num1 * den2 - num2 * den1
    return make_rational(numer, denom)

def rat_to_string(rat):
    return '{}/{}'.format(get_numer(rat),get_denom(rat))


if __name__ == '__main__':
    rat1 = make_rational(1,3)
    rat2 = make_rational(12,3)
    print(rat_to_string(rat1))
    print(rat_to_string(rat2))
    rat3 = add(rat1, rat2)
    rat4 = sub(rat1, rat2)
    print(rat_to_string(rat3))
    print(rat_to_string(rat4))
    rat5 = add(rat3, rat4)
    rat6 = sub(rat3, rat4)
    print(rat_to_string(rat5))
    print(rat_to_string(rat6))





