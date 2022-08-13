from Student_Admissions import Student


class Chosecourse(Student):

    def __init__(self, student_id, mark, age, fees, couse_id=1001):
        super().__init__(student_id, mark, age)
        self.__course_id = couse_id
        self.__fees = fees

    def get_fees(self):
        return self.__fees

    def choose_course(self):
        print("**********************")
        if (self.__course_id == 1001) or (self.__course_id == 1002):
            print("**********************")
            if (Student().self.__mark > 85):
                Student.self.__fees = self.__fees - (self.__fees * (25/100))
                print(self.__fees)

            else:
                return True
        else:
            return False


suresh = Chosecourse(10, 90, 20,  25575)
print(suresh.get_fees())
suresh.choose_course()
print(suresh.get_fees())
