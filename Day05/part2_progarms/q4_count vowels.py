def count_vowels(name):
    vowels = "aeiouAEIOU"
    return sum(1 for char in name if char in vowels)
print(count_vowels("Hello World"))