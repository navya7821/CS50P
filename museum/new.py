import sys
def main():
    name=input()
    hello(name)
    goodbye(name)

def hello(name):
    print("Hello",name)
def goodbye(name):
    print("Goodbye",name)
if __name__ == '__main__':
    main()
