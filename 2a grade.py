name=input("ENTER THE NAME:")
p=int(input("ENTER THE PHYSICS MARK:"))
c=int(input("ENTER THE CHEMISTRY MARK:"))
m=int(input("ENTER THE MATHS MARK:"))
tot=p+c+m
avg=(tot)/3
print("NAME:",name)
if avg>90:
    print("PASS---> S GRADE")
elif avg>80:
    print("PASS---> A GRADE")
elif avg>70:
    print("PASS---> B GRADE")
elif avg>60:
    print("PASS---> C GRADE")    
elif avg>=50:
    print("PASS---> D GRADE")
else:
    print("FAIL---> F GRADE")

print("AVERAGE=",avg)    
