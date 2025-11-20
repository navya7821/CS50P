def convert(time):
    a,b=time.split(":")
    a=float(a)
    b=float(b)
    b=float(b/60)
    return a+b

def main():
    s=input("Time : ").strip()
    c = convert(s)
    if c is not None:
        if 7<=c<=8:
            print("breakfast time")
        elif 12<=c<=13:
            print("lunch time")
        elif 18<=c<=19:
            print("dinner time")
        else:
            return

if __name__ == "__main__":
    main()



