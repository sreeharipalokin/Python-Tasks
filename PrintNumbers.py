# to print numbers from 1 to 20
# except multiples of 2 and 3

print("Numbers Are as follows")
for number in range(1,21):
    if number %2 == 0 or number %3 == 0:
        pass
    else:
        print(number)