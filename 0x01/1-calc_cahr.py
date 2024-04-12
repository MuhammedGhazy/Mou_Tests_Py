#!/python3
count = 0
vowels = {'a', 'e', 'i', 'o', 'u'}
name = input("Please Enter Your Name: ")
for char in name:
    if char in vowels:
        count += 1

print(f"Your Name is {name}, And The Sum Of Vowels is {count}")

