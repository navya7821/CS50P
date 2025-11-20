import re
import sys
def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r"\"https?://(www\.)?youtube\.com/embed/.+\"(\>| title)"
    mi = re.search(pattern,s)
    if mi:
        mi = mi.group()
        mi = mi.replace("youtube.com/embed","youtu.be")
        mi = mi.replace("www.",'')
        mi = mi.replace("http:","https:")
        mi = mi.replace(" title","")
        mi = mi.replace('>','')
        mi = mi.replace('"','')
        return mi
    else:
        return None





if __name__ == "__main__":
    main()
