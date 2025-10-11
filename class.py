class car:
    '''about the car'''
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("car starting")
        print(f"car make: {self.make}")
        print(f"car model: {self.model}")
        print(f"car year: {self.year}")
    def stop(self):
        print("car stopping")
        print(f"car make: {self.make}")
        print(f"car model: {self.model}")
        print(f"car year: {self.year}")
car1=car(2007,"nano",2009)
car1.start()
car1=car(2006,"nan",2001)
car1.stop()
         
         
        
    
