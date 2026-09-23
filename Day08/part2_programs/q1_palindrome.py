s=input("Enter a string: ").lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

is_pal=True 
l=0
r=len(s)-1
while l<r:
    if s[l]!=s[r]:
        is_pal=false
        break
    l+=1
    r-=1
print(is_pal)