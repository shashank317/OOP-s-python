class Class:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks 

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.__marks}")
    
    def update_marks(self, new_marks):
        if 0 <= new_marks <=100:
            self.__marks = new_marks
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")

s1 = Class("Shashank", 85)
s1.show_details()

s1.update_marks(70)
s1.show_details()



# s1.__marks  ❌ This will give error (private)


     