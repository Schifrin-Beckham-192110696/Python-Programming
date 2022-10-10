def vote(age):
 if age>0:
    if(age>=18):
        print("YOU ARE ALLOWED TO VOTE")
    else:
        print("YOU ARE ALLOWED TO VOTE AFTER",18-age,"YEARS")
 elif age==0:
     print("AGE CANNOT BE ZERO")
 else:
     print("NEGATIVE NUMBER")
     
try:
    age=int(input("ENTER THE AGE:"))
    vote(age)
except ValueError:
    print("INVALID INPUT")
        
