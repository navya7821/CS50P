import random
def main():
    temp_num = get_level()

    score = 0
    for _ in range(10):
        x = generate_integer(temp_num)
        y = generate_integer(temp_num)
        i = 0
        while i < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x+y:
                    score +=1
                    break
                else:
                    print('EEE')
                    i +=1
            except ValueError:
                print('EEE')
                i +=1
        if i == 3:
            print(f"{x} + {y} = {x+y}")

    print("Score: " ,score)




def get_level():
    while True:
        try:
            ans = int(input("Level: "))
            if not ans in [1,2,3]:
                raise Exception
            return ans
        except ValueError:
            pass
        except Exception:
            pass

def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError
    if level == 1:
        a = 0
        b = 9
    elif level == 2:
        a = 10
        b = 99
    elif level == 3:
        a = 100
        b = 999

    x = random.randint(a,b)

    return x



if __name__ == "__main__":
    main()
