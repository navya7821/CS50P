sum=0
while sum < 50:
    coin=(input("Insert coin:"))
    if coin.isdigit():
           coin=int(coin)
           if coin==25 or coin==5 or coin==10:
               sum=sum+coin

               if sum<50:
                   balance=50-sum
                   print(f"Amount Due: {balance}")
               else:
                   print(f"Change Owed: {sum-50}")
           else:
                if sum==0:
                     print("Amount Due: 50")
                else:
                     print(f"Amount Due: {balance}")
    else:
        print("Integers only")
        break

