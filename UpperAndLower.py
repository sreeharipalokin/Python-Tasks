string = input("Enter a string : ")

def Counter(string):
    counter1 = 0
    counter2 = 0

    for characters in string:
        if characters.isupper():
            counter1 += 1
        elif characters.islower():
            counter2 += 1
        else:
            pass
    print(f"Uppercase letter : {counter1}, Lowercase letter : {counter2}")

Counter(string)