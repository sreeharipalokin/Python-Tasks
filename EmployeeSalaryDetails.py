employee_id = int(input("Enter Employee ID : "))
employee_name = input("Enter Employee Name : ")
basic_pay = int(input("Enter Basic Pay : "))

print(f"Employee Name : {employee_name}\nEmployee ID : {employee_id}")
if basic_pay > 10000:
    HRA = (basic_pay*15)/100
    DA = (basic_pay*8)/100
    Net_Pay = basic_pay + DA + HRA
    
    print(f"HRA : {HRA} Rs. , DA : {DA} Rs. , Net Pay : {Net_Pay} Rs.")
elif basic_pay > 5000 and basic_pay <=10000:
    HRA = (basic_pay*10)/100
    DA = (basic_pay*5)/100
    Net_Pay = basic_pay + DA + HRA

    print(f"HRA : {HRA} Rs. , DA : {DA} Rs. , Net Pay : {Net_Pay} Rs.")
elif basic_pay <= 5000:
    HRA = (basic_pay*5)/100
    DA = (basic_pay*3)/100
    Net_Pay = basic_pay + DA + HRA
    print(f"HRA : {HRA} Rs. , DA : {DA} Rs. , Net Pay : {Net_Pay} Rs.")
else:
    pass


