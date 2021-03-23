class Gym:
    c=''
    def __init__(self,n,g,a,w,h):
        self.name=n
        self.gender=g
        self.age=a
        self.weight=w
        self.height=h
        Gym.c='Thank-You'
        return
    def CalcBmi(self):
        bmi=self.weight/(self.height**2)
        return bmi
    def ShowInfo(self,bmi):
        print("Your Info:\n 1.Name:",self.name,"\n 2.Sex:",self.gender,"\n 3.Age:",self.age,"\n 4.Weight:",self.weight,"\n 5.Height:",self.height,"\n\t\t BMI:",round(bmi,2),end="(")
        return
    @classmethod
    def Thankyou(cls,bmi):
        if bmi<16:
            print("Severe Thinness)")
        elif bmi>=16 and bmi<17:
            print("Moderate Thinness)")
        elif bmi>=17 and bmi<18.5:
            print("Mild Thinness)")
        elif bmi>=18.5 and bmi<25:
            print("Normal)")
        elif bmi>=25 and bmi<30:
            print("Overweight)")
        elif bmi>=30 and bmi<35:
            print("Obese Class I)")
        elif bmi>=35 and bmi<40:
            print("Obese Class II)")
        else:
            print("Obese Class III)")

        print("\n",cls.c)
        return




print("Welcome to Fitness Club01")
name=input("enter your name:\t")
gender=int(input("Enter gender:\n1.Male\n2.Female\n3.Others:\t"))
if gender==1:
    gender='Male'
elif gender==2:
    gender='Female'
else:
    gender='Trans-gender'
age=int(input("Enter your age:\t"))
weight=float(input("Enter your weight in kg:\t"))
height=float(input("Enter your height in metres:\t"))
g=Gym(name,gender,age,weight,height)
bmi=g.CalcBmi()
g.ShowInfo(bmi)
g.Thankyou(bmi)
