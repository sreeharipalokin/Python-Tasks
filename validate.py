from datetime import date,datetime
# phonenumber="123456780"
# def validatePhonenumber():
#     phonepattern = r'^\d{10}$'
#     matchs = re.match(phonepattern,phonenumber)
#     if((phonenumber == "") or (matchs is None)):
#         return False
#     else:
#         return True        

# v= validatePhonenumber()
# print(v)

def validateDate():
    today = str(date.today())
    dob = "2000-01-01"
    date1 = datetime.strptime(today,"%Y-%m-%d")
    date2 = datetime.strptime(dob,"%Y-%m-%d")
    diff = date1 - date2
    print(diff.days/365.25)
validateDate()  