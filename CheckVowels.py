vowels = ['a','e','i','o','u','A','E','I','O','U']
# vowels_present = []
counter = 0
string = input("Enter a string : ")
for character in string:
    for item in vowels:
        if character==item:
            # vowels_present.append(character)
            counter += 1

print(f"{counter} vowels present")

