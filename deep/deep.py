m=input("What is answer to the Great Question of Life,the Universe and Everything? ")

def sub(s):
      s=s.strip().lower() #remove whitespaces
      s=s.replace("-"," ")#remove hyphen
      #s=s.lower()#case insensitive
      c=s.split()#space insensitive
      if c==["forty","two"]:
          print("Yes")
      else:
        print("NO")

if(m.strip()=="42"):
   print("Yes")
else:
     sub(m)
