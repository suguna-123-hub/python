class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        return f"Name:{self.name},marks:{self.marks}"
s1=student("padma",85)
s2=student("ram",90)
print(s1.display_info())
print(s2.display_info())
