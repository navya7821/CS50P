def main():
    phrase=input("Greeting: ")
    fee = value(phrase)
    print(f'${fee}')

def value(final):
    final = final.strip().lower()
    final = final.split()
    if len(final[0]) == 5:
        if final[0] == 'hello':
                return 0
        elif final[0][0] == 'h':
                return 20
        else:
                return 100

    elif len(final[0])>5 and final[0][0]=='h' and final[0][1]=='e' and final[0][2]=='l' and final[0][3]=='l' and final[0][4]=='o' and final[0][5] in ['!',',']:
        return 0

    elif(final[0][0]=="h"):
        return 20

    else:
        return 100

if __name__ == '__main__':
    main()
