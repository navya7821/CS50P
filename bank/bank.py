greeting=input("Greeting: ")
greeting=greeting.strip().lower()
final=greeting.split()

final = final.strip().lower()
final = final.split()
if len(final[0]) == 5:
        if final[0] == 'hello':
            print('$0')
        elif final[0][0] == 'h':
            print('$20')
        else:
            print('$100')
elif len(final[0])>5 and final[0][0]=='h' and final[0][1]=='e' and final[0][2]=='l' and final[0][3]=='l'and final[0][4]=='o'and  final[0][5] in [',','!']:
            print('$0')
elif(final[0][0]=="h"):
        print('$20')
else:
        print('$100')
