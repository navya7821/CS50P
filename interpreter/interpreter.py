def main():
    s=input("Expression: ").strip()
    x,y,z=s.split()
    if(y!="+" and y!="-" and y!="*" and y!="/"):
        print("Enter a valid operator")
        return
    elif(y=="/" and z=="0"):
        print("Division by zero is not possible")
        return

    x=int(x)
    z=int(z)
    calculator(x,y,z)

def calculator(a,b,c):
    match b:
        case "+":
            print(f"{a+c:.1f}")
        case "-":
            print(f"{a-c:.1f}")
        case "*":
            print(f"{a*c:.1f}")
        case "/":
            print(f"{a/c:.1f}")

main()
