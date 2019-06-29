'''class Patient():
    def __init__(self,name,age,gender,disease): #initializer
############attribute
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
###########behiviour
    def take_medicine():
        print(f"{self.name} is taking medicine")
    def take_rest():
        print(f"{self.name} is taking rest")
    def deposit_Money():
        print(f"{self.name} is depositing fee")

p1 = Patient("gabbar",50,"male","flu")

p2 = Patient("samba",56,"male","fever")'''

'''class Student():
    def __init__(self,name,f_name,age,gender,standard): #initializer
############attribute
        self.name = name
        self.f_name = f_name
        self.age = age
        self.gender = gender
        self.standard = standard
###########behiviour
    def take_scheduled_class():
        print(f"{self.name} is taking scheduled classes")
    def take_exams():
        print(f"{self.name} is taking exams")
    def take_buy_course():
        print(f"{self.name} is buying couse")
    def deposit_fee():
        print(f"{self.name} is depositing fee")

s1 = Student("annu","qamar",21,"male",8)

s2 = Student("sarah","raheem",20,"female",7)'''

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoeter_reading = 0
        
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+seld.model
        return long_name.title()
    def read_odomoter():
        print(f"the car has travelled {self.odomoeter_reading} miles")

my_new_car = Car('audi','a4',2016)

