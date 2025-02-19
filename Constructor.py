class STUDENT:
    def __init__(self, name, course, sex, result):
        self.name = name
        self.course = course
        self.sex = sex
        self.result = result

    def display(self):
        print("Name: ", self.name)
        print("Course: ", self.course)
        print("Sex: ", self.sex)
        print("Result: ", self.result)


s = STUDENT("Hell", "Java", "Male", "90%")
s.display()
