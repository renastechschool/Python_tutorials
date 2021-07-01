#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

# Class definitions, like function definitions (def statements) must be executed before they
# have any effect. (You could conceivably place a class definition in a branch of an if
# statement, or inside a function.)

class greeting:
    name="a name"

    def say_hello(self):
        return "Hello "+ self.name

    def  say_goodbye(self):
        return "Goodbye "+ self.name

a_person=greeting()
#print(a_person.name)
#print(a_person.say_hello())
#print(a_person.say_goodbye())

a_person.name="John"
print(a_person.name)
print(a_person.say_hello())
print(a_person.say_goodbye())
#===================================================#

class personal_info:
    def __init__(self, name, lastname, country, gender):
        self.name=name
        self.lastname=lastname
        self.country=country
        self.gender=gender

    def get_name(self):
        return "Your name is {}".format(self.name)
    def get_country(self):
        return "You are from {}".format(self.country)
    def get_gender(self):
        return "Your gender is {}".format(self.gender)
person1=personal_info("Haluk", "Akpinar","Turkey","Male")
print(person1.name)
person1.name="Hasan"
print(person1.name)

print(person1.get_country())



###====================================##

class clock:
    time="8:06"
    def get_time(self):
        return self.time
class calendar:
    date="06/30/2021"
    def get_date(self):
        return self.date
class calendarClock (clock, calendar):
    pass

timedate=calendarClock ()
print (timedate.get_time())
print (timedate.get_date())


class calculate_bmi2:

    def __init__(self, height, weight, measurement):
        self.height=height
        self.weight=weight
        self.measurement=measurement

    def cal_bmi(self):
        if self.measurement=="cm":
            bmi=self.weight/(self.height*0.01)**2
        if self.measurement=="m":
            bmi=self.weight/self.height**2
        return bmi

    def health_condition(self):
        get_bmi = self.cal_bmi()
        if get_bmi < 18.5:
            return "You are underweight"
        if 18.5 < get_bmi < 24.9:
            return "You have normal weight"
        if 25 < get_bmi < 29.9:
            return "You are overweight"
        if get_bmi > 30:
            return "You are obes"

class personal_info2 (calculate_bmi2):
    name="Hasim"
    lastname="Engin"
    dob=1985
    year=2021

    def get_name(self):
        return "Hi " + self.name + " " + self.lastname

    def calculate_age(self):
        age = self.year - self.dob
        return age


my_info=personal_info2 (187,80,"cm")
print(my_info.height)
print(my_info.weight)
print(my_info.health_condition())
print(my_info.cal_bmi())
print(my_info.calculate_age())


