class Student:
    school_name= 'D.A.V.S.K.V.B'
    Principal_name= 'Mrs. Bhuvaneshwori Rao'
    def __init__(self, student_f_name , student_l_name):
        self.first_name = student_f_name
        self.last_name = student_l_name

        def get_name(self):
            return self.first_name


    @classmethod
    def get_school_name(cls):
            return cls.school_name

    @staticmethod
    def add (a,b):
            print (a+b)




s =  Student ('shivani' ,'puri')
print (Student.get_school_name())

Student.add(2,3)
