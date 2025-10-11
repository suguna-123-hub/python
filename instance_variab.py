class student:
    def __init__(self,name,rol_no):
      self.name=name
      self.rol_no=rol_no
      print("name:",self.name)
      print("rollno:",self.rol_no)
    def marks(self,marks):
      self.marks=marks
      print("marks:",self.marks)
s1=student("sugu",419)
s1.marks(90)
s2=student("pallu",512)
s2.marks(68)
s3=student("nandhu",532)
s3.marks(91)
s4=student("niha",533)
s4.marks(88)
s5=student("anu",532)
s5.marks(91)    
