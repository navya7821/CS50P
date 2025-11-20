import validators
mail = input("What's your email address? ")
x = validators.email(mail)
if x == True:
        print('Valid')
else:
        print('Invalid')

