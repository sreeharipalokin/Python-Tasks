class Student:

    def __init__(self):
       self.roll_number = 1
       self.student_name = "Default"
       
    
    def get_data(self):
        self.name_and_roll = []
        roll_num = int(input("Enter Roll : "))
        stud_name = input("Enter Name : ")
        self.roll_number = roll_num
        self.student_name = stud_name
        self.name_and_roll.append(self.student_name)
        self.name_and_roll.append(self.roll_number)


    def print_data(self):
        return self.name_and_roll
        

class Marks(Student):

    def __init__(self):
        self.subject_1 = self.subject_2 = self. subject_3 = 0
        self.subject_4 = self.subject_5 = self. subject_6 = 0
    
    def input_data(self):
        super().get_data()
        self.subject_1 = int(input("Enter Marks for Mathematics : "))
        self.subject_2 = int(input("Enter Marks for Physics : "))
        self.subject_3 = int(input("Enter Marks for Chemistry : "))
        self.subject_4 = int(input("Enter Marks for Botany : "))
        self.subject_5 = int(input("Enter Marks for Computer Science : "))
        self.subject_6 = int(input("Enter Marks for Geography : "))
    
    def out_data(self):
        details = super().print_data()
        total_mark = [
            self.subject_1,
            self.subject_2,
            self.subject_3,
            self.subject_4,
            self.subject_5,
            self.subject_6
            ]

        final_result = {
            0:f"Name : {details[0]}",
            1:f"Roll Number : {details[1]}",
            2:f"Marks obtained for Mathematics : {self.subject_1}",
            3:f"Marks obtained for Physics : {self.subject_2}",
            4:f"Marks obtained for Chemistry : {self.subject_3}",
            5:f"Marks obtained for Botany : {self.subject_4}",
            6:f"Marks obtained for Computer Science : {self.subject_5}",
            7:f"Marks obtained for Geography : {self.subject_6}",
            8:f"Total Marks Obtained : {sum(total_mark)}"
        }       
        return final_result

stud_marks = Marks()
stud_marks.input_data()
details = stud_marks.out_data()
print("\n")
for detail,value in details.items():
    print(value)
