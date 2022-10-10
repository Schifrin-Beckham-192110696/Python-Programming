def perf(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if n==sum:
        print("Perfect number")
    else:
        print("Not a Perfect Number")

try:
    n=int(input("ENTER THE N VALUE:"))
    perf(n)
except ValueError:
    print("INVALID")
