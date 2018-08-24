class Cls1:
    
    'python program with class and function'
    def __init__(self,sname,slastname,smobile_nom,s_age):
        self.sname=sname
        self.slastname=slastname
        self.smobile_nom=smobile_nom
        self.s_age=s_age
#   def Entry(self):
 #       sname=str(raw_input("Enter Your First Name :"))
  #      slastname=str(raw_input("Enter Your Last Name :"))
   #     smobile_nom=raw_input("Enter Your Mobile number :")
    #    s_age=raw_input("Enter Your Age :")
        
    def Display(self):
        print "First name : ",self.sname,"Last name : ",self.slastname,"Mobile number :",self.smobile_nom,"Age : ",self.s_age

#dEntry=Cls1(sname="savan",slastname="katara",smobile_nom=12345678,s_age=12)
dEntry=Cls1(sname,slastname,smobile_nom,s_age)
sname=str(raw_input("Enter Your First Name :"))
slastname=str(raw_input("Enter Your Last Name :"))
smobile_nom=raw_input("Enter Your Mobile number :")
s_age=raw_input("Enter Your Age :")
#Cls1.Entry()

dEntry.Display()
