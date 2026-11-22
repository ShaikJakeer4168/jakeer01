#Program 1: Vowels and Consonants
name = input("Enter your name: ")
v = 0
c = 0
for i in name:
    if i in "aeiou":
        v += 1
    else:
        c += 1
print("Number of vowels:", v)
print("Number of consonants:", c)
