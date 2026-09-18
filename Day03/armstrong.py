#1.Armstrong number
num = int(input("Enter a number: "))
temp=num
total=0
while temp>0:
    digit=temp%10
    total+=digit**3
    temp//=10
if total==num:
    print("Armstrong")
else:
    print("Not Armstrong")


print("\nPattern:")
for i in range(1,6):
    print("*"*i)