def revnum(n):
    rev=0
    while(n!=0):
      d=n%10
      rev=rev*10+d
      n=n//10
    print("REVERSED NUMBER=",str(rev))

try:
  n=int(input("ENTER THE N VALUE:"))
  if(n<0):
      print("NEGATIVE NUMBER")
  else:    
      revnum(n)
except ValueError:
    print("NOT A NUMBER")
