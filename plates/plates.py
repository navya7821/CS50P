import string
def main():
    st = input("PLATE: ")
    if st=='':
       print("Invalid")
       return
    elif len(st) <2 or len(st)>6:
        print("Invalid")
        return
    elif punc(st):
       print("Invalid")
       return
    elif st[0].isdigit() or st[1].isdigit():
        print("Invalid")
        return
    elif len(st)==2:
        print("Valid")


    elif st[2]=='0':
        print("Invalid")
    elif len(st)==3:
        print("Valid")


    elif len(st)==4 and st[2].isdigit():
        if st[2]=='0':
            print("Invalid")
        elif st[3].isdigit():
            print("Valid")
        else:
            print("Invalid")
    elif len(st)==4:
        print("Invalid")



    elif len(st)==5 and st[2].isdigit():
        if st[2]=='0':
            print("Invalid")
        elif st[3].isdigit() and st[4].isdigit():
            print("Valid")
        else:
            print("Invalid")
    elif len(st)==5 and st[3].isdigit():
        if st[3]=='0':
            print("Invalid")
        elif st[4].isdigit():
            print("Valid")
        else:
            print("Invalid")
    elif len(st)==5:
        print("Valid")


    elif len(st)==6 and st[2].isdigit():
        if st[2]=='0':
            print("Invalid")
        elif st[3].isdigit() and st[4].isdigit() and st[5].isdigit():
            print("Valid")
        else:
            print("Invalid")
    elif len(st)==6 and st[3].isdigit():
        if st[3]=='0':
            print("Invalid")
        elif st[4].isdigit() and st[5].isdigit():
            print("Valid")
        else:
            print("Invalid")
    elif len(st)==6 and st[4].isdigit():
        if st[4]=='0':
            print("Invalid")
        elif st[5].isdigit():
            print("Valid")
        else:
            print("Invalid")
    elif len(st)==6 :
        print("Valid")
def punc(st):
    for char in st:
        if char in string.punctuation or char.isspace():
            return True
    return False

main()
