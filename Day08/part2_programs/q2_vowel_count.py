s = input("Enter string: ").lower()

# Program 1: Vowel count
vowels = "aeiou"
count = 0
for ch in s:
    if ch in vowels:
        count+=1
print("Vowel count:", count)

# Program 2: Reverse string without [::-1]
rev = ""
for ch in s:
    rev = ch + rev
print("Reverse:", rev)

# Program 3: Word count
words = s.split()
print("Word count:", len(words))