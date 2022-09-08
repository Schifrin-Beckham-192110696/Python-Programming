def revstr(s):
    s1=""
    for i in s:
        s1=i+s1
    print("REVERSED STRING:",s1)
s=input("ENTER THE STRING:")
ca1=int(s)
if(ca1>=0):
    print("NUMBERS")
else:    
  revstr(s)

