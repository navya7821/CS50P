import re
import sys
def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):

    pattern = r"^((25[0-5]|2[0-4]\d|1\d\d|\d\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|\d\d|\d)$"
    op = re.search(pattern,ip.strip())
    
    if op:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
