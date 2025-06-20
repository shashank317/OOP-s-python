class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"student name is {self.name} and \nhis marks is {self.marks}")

student1 = Students("sha",90)
student2 = Students("sai",95)

student1.display()
student2.display()