
class student:

    school = 'Telsuko'

    def __init__(self,m1,m2,m3) :
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print('The name is .....')
        
s1 = student(45,78,95)
s2 = student(25,85,35)

print(s1.avg())
print(student.getschool())
student.info()

#sample output
#72.66666666666667
#Telsuko
#The name is .....