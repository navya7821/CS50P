import string
def main():
    plate = input('PLATE: ')
    if is_valid(plate):
        print('Valid')
    else :
        print('Invalid')



def is_valid(s):
    if any(char in string.punctuation for char in s):
        return False
    pass
    #print('Punctuation test passed')
    #print(len(s))
    if len(s) < 2 or len(s) > 6:
        #print('Check')
        return False
    pass
    if s[0].isdigit() or s[1].isdigit():
        return False
    pass

    if len(s) == 2:
        return True

    if len(s) == 3:
        if s[2] == '0':
            #print(s[2])
            return False
        else:
            return True

    if len(s) == 4:
        if s[2].isdigit():
            if s[2] == '0':
                return False
            elif not s[3].isdigit():
                return False
            else:
                return True

        elif s[3].isdigit():
            if s[3] == '0':
                return False
            else:
                return True
        else:
            return True

    if len(s) == 5:
            if s[2].isdigit():
                if s[2] == '0':
                    return False
                elif not s[3].isdigit() and s[4].isdigit():
                    return False
                else:
                    return True

            elif s[3].isdigit():
                if s[3] == '0':
                    return False
                elif not s[4].isdigit():
                    return False
                else:
                    return True

            elif s[4].isdigit():
                if s[4] == '0':
                    return False
                else:
                    return True
            else:
                return True

    if len(s) == 6:
        if s[2].isdigit():
            if s[2] == '0':
                return False
            elif not s[3].isdigit() and s[4].isdigit() and s[5].isdigit():
                return False
            else:
                return True
        elif s[3].isdigit():
            if s[3] == '0':
                return False
            elif not s[4].isdigit() and s[5].isdigit():
                return False
            else:
                return True
        elif s[4].isdigit():
            if s[4] == '0':
                return False
            elif not s[5].isdigit():
                return False
            else:
                return True
        elif s[5].isdigit():
            if s[5] == '0':
                return False
            else:
                return True
        else:
            return True



if __name__ == "__main__":
    main()
