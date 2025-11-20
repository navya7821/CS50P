import sys
def main():

    fuel = input('Fraction: ')
    num = convert(fuel)
    final = gauge(num)
    print(final)


def convert(frac):
        num,den = frac.split('/')
        num = int(num)
        den = int(den)
        if den == 0:
            raise ZeroDivisionError
        elif num>den:
            raise ValueError
        perc = num/den
        perc = perc*100
        perc = round(perc)
        return perc

def gauge(ans):
    if ans <= 1:
        return 'E'
    elif ans >= 99:
        return 'F'
    else:
        return f"{ans}%"

if __name__ == '__main__':
    main()
