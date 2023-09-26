print("Enter Marks of :")
subject_1 = int(input("Subject 1 : "))
subject_2 = int(input("Subject 2 : "))
subject_3 = int(input("Subject 3 : "))
subject_4 = int(input("Subject 4 : "))
subject_5 = int(input("Subject 5 : "))
subject_6 = int(input("Subject 6 : "))

total = subject_1+subject_2+subject_3+subject_4+subject_5+subject_6

avg = total/6

print(f"Total Marks Obtained : {total}, Average is {avg}")


def Grade(value):
    if value >= 90:
        return "A+"
    elif value >= 80 and value <90:
        return "A"
    elif value >= 70 and value <80:
        return "B+"
    elif value >= 60 and value <70:
        return "B"
    elif value >=50 and value <60:
        return "C+"
    elif value >=40 and value <50:
        return "C"
    elif value >=30 and value <40:
        return "D+"
    else:
        return "Failed"

result = Grade(avg)

print(f"Overall Grade : {result}")

    