class Student():
    __student_id = None
    __mark = None
    __age = None

    def __init__(self, student_id, mark, age):
        self.__student_id = student_id
        self.__mark = mark
        self.__age = age

    def set_mark(self, mark):
        self.__mark = mark

    def get_mark(self):
        return self.__mark

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def validate_marks(self):
        if (self.__mark > 0 and self.__mark < 100):
            return True
        else:
            return False

    def validate_age(self):
        if (self.__age > 0 and self.__age < 21):
            return True
        else:
            return False

    def Check_qualification(self):
        if (self.validate_age() and self.validate_marks()):
            if (self.__mark >= 65):
                return True
            else:
                return False
        else:
            return False


Ram = Student(20, 70, 17)
print(Ram.validate_marks())
print(Ram.validate_age())
print(Ram.Check_qualification())
Ram.set_mark(int(input("The mark ")))
print(Ram.validate_marks())
print(Ram.validate_age())
print(Ram.Check_qualification())
print(Ram.get_mark())
Ram.set_age(22)
print(Ram.validate_marks())
print(Ram.validate_age())
print(Ram.Check_qualification())
print(Ram.get_age())
