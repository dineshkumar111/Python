

class student:

    def __init__(self,m1,m2) -> None:
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):

        s=0

        if a!=None and b!=None and c!=None:

            s=a+b+c
        
        elif a!=None and b!=None:

            s=a+b

        return s


s1=student(56,85)

print(s1.sum(2,5,8))
