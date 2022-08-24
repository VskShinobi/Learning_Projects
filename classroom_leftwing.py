class Classroom:
    classroom_list = []

    @staticmethod
    def search_classroom(class_room):
        for i in Classroom.classroom_list:
            if i == class_room:
                print("Found")
                break
            else:
                continue
        else:
            print("-1")

    @staticmethod
    def set_class_list(class_list):
        Classroom.classroom_list = class_list

    @staticmethod
    def get_class_list():
        return Classroom.classroom_list


class_list = ['a', 'b', 'c', 'd']
Classroom.set_class_list(class_list)
print(Classroom.get_class_list())
Classroom.search_classroom('a')
print(Classroom.classroom_list)
