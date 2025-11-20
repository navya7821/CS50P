import sys
def main():
        s=input("Input: ")
        output = shorten(s)
        print(output)


def shorten(word):
    proc_word = ''.join([char for char in word if char not in ['a','e','i','o','u']])
    return proc_word


if __name__ == '__main__':
    main()
