

class student:

    def __init__(self,m1,m2) -> None:
        self.m1=m1
        self.m2=m2


    def __add__(self,other):
        m1=self.m1+self.m1
        m2=self.m2+self.m2
        s3=student(m1,m2)
        return s3


s1=student(52,85)
s2=student(45,87)

s3=s1+s2

print(s3.m1)
