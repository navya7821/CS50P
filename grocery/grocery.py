prod ={}
while True:
    try:
        key= input().upper()
        if key in prod.keys():
            prod[key] +=1
        else:
            prod[key] = 1

    except EOFError:
        break
sor_list = dict(sorted(prod.items()))
for item in sor_list:
    print(sor_list[item],item)



