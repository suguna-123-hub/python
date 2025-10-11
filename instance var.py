class Student:
    def __init__(self, name, roll_no):  
        self.name = name
        self.roll_no = roll_no
        print("inside constructor:")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
    def update_marks(self, marks):
        self.marks = marks
        print("\nInside instance method:")
        print(f"{self.name}'s Marks updated to:", self.marks)
s1 = Student("sugu", 101)        
print("\nOutside of class:")
print("Name(after):", s1.name)
s1.update_marks(85)
print("Marks(outside):", s1.marks)
