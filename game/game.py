import random
while True:
    try:
        level = int(input('Level: '))
        if level <= 0:
            raise Exception
        break
    except ValueError:
        pass
    except Exception:
        pass

number = random.randint(1,level)

while True:
    try:
        guess = int(input('Guess: '))
        if guess < 0:
            raise ValueError
        if number == guess:
            print('Just right!')
            break
        elif number > guess:
            print('Too small!')
        elif number < guess:
            print('Too large!')
    except ValueError:
        pass







