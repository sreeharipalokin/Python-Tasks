# convert length from 'centimeter' to  'inches'

length = int(input("Enter length (in centimeter) : "))

if length <= 0:
    print("Invalid entry")
else:
    length_inches = length*(1/2.54)
    length_inches = round(length_inches,5)
    print(f"Length in inches {length_inches}")

