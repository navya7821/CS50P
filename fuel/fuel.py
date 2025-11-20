while True:
    try:
        frac = input("Fraction: ")
        num,den = frac.split('/')
        num = int(num)
        den = int(den)
        perc = num/den
        if num>den:
            raise Exception

    except ZeroDivisionError:
        pass
    except ValueError:
        pass
    except Exception:
        pass
    else:
        break

perc = perc*100
perc = round(perc)
if perc <= 1:
    print('E')
elif perc >= 99:
    print('F')
else:
    print(f"{perc}%")






