def main():
    s = input("camelCase:  ")
    indices=[index for index ,char in enumerate(s) if char.isupper()]

    if len(indices)==0:
        print(f"snake_case: {s}")
        return
    i=-1
    s=s.lower()
    string=[]

    while i <(len(indices)-1):
        if i ==-1:
            st=s[0:indices[i+1]]
            i+=1
        else:
            st=s[indices[i]:indices[i+1]]
            i+=1
        string.append(st)

    stri=s[indices[len(indices)-1]:]
    string.append(stri)
    x=0
    print('snake_case:',end=' ')
    while x < (len(string)-1):
        print(string[x],end='_')
        x+=1
    print(string[len(string)-1])


main()




