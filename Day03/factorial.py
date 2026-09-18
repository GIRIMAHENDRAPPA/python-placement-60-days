n=int(input("enter a number:"))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(f"factorial of {n} is {fact}")