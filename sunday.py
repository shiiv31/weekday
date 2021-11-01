class Student:
    def __init__(self, student_f_name , student_l_name):
        self.first_name = student_f_name
        self.last_name = student_l_name

s =  Student ('shivani' ,'puri')
print (s.first_name , s.last_name)