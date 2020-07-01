student_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", 
"Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

class Garden:
    def __init__(self, diagram, students = student_list):

        self.diagram = diagram.splitlines()
        self.students = students
        self.students.sort()

    def plants(self, name):

        return_list = []

        flower_dict = {"V":"Violets", "G": "Grass", "C":"Clover", "R":"Radishes"}

        student_number = (self.students.index(name)) * 2

        return_list.append(flower_dict.get(self.diagram[0][student_number]))
        return_list.append(flower_dict.get(self.diagram[0][student_number + 1]))
        return_list.append(flower_dict.get(self.diagram[1][student_number]))
        return_list.append(flower_dict.get(self.diagram[1][student_number + 1]))
        return return_list