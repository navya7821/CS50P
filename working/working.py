import re
import sys
def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(?P<hr1>([0-9]|1[0-2]){1,2})(?P<min1>(\:[0-5][0-9])?) (PM|AM) to (?P<hr2>([0-9]|1[0-2]){1,2})(?P<min2>(\:[0-5][0-9])?) (PM|AM)$"
    x = re.search(pattern,s.strip())
    if not x:
        raise ValueError
    a,b = x.group().split('to')
    a,b = a.strip(),b.strip()
    c = int(x.group('hr1'))
    d = int(x.group('hr2'))
    if a[-2:] == 'PM':
        if c == 12:
            a1 = 12
        else:
            a1 = c +12
    elif a[-2:] == 'AM':
        if c == 12:
            a1 = 0
        else:
            a1 = c

    if x.group('min1') == '':
        a2 = 0
    else:
        a2 = int(x.group('min1').replace(':','').strip())

    if b[-2:] == 'PM':
        if d == 12:
            b1 = 12
        else:
            b1 = d+12
    elif b[-2:] == 'AM':
        if d == 12:
            b1 = 0
        else:
            b1 = d

    if x.group('min2') == '':
        b2 = 0
    else:
        b2 = int(x.group('min2').replace(':','').strip())

    return f"{a1:02}:{a2:02} to {b1:02}:{b2:02}"


if __name__ == "__main__":
    main()
