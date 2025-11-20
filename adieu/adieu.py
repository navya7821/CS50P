
def main():
    pr_string = 'Adieu, adieu, to '
    i = 0
    while i<1:
        try:
            name1 = input("Name: ")
            pr_string = pr_string + name1
            i+=1
        except EOFError:
            print()
            return
    while i <2:
        try:
           name2= input("Name: ")
           pr_string = pr_string + ' and ' + name2
           i+=1
        except EOFError:
            print()
            print(pr_string)
            pr_string = pr_string.replace(', and',',')
            return


    while True:
        try:
            name = input("Name: ")
            pr_string = pr_string.replace(' and',',')
            pr_string = pr_string + ',' + ' and ' + name
        except EOFError:
            print()
            break
    pr_string = pr_string.replace(',,',',')
    print(pr_string)





main()


