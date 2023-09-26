# program to validate credentials

# function to check Password
def Password():
    password_1 = input("Enter Password : ")
    password_2 = input("Re-Enter Password : ")
    if password_1 == password_2:
        return "All Credentials Matched Successfully"
    else:
        return "Mismatch in Password"

def Username():
    username_1 = input("Enter Username : ")
    username_2 = input("Re-Enter Username : ")
    if username_1 == username_2:
        print("Incorrect Username")
        return Password()   
    else:
        return "Mismatch in Username"

result = Username()
print(result)



