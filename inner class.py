
class student:

    def __init__(self,name,rollno) -> None:
        self.name=name 
        self.rollno=rollno
        self.lap=self.laptop()
        

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()


    class laptop:

        def __init__(self) -> None:
            self.name="Lenovo"
            self.cpu="i5"
            self.ram='8 GB'

        def show(self):
            print(self.name,self.cpu,self.ram)

           
s1=student("Dinesh",3)
s1.show()

#lap1=student.laptop()
#lap1.show()   
#we can use this without reference for the self...stuf....

#sample output
#Dinesh 3
#Lenovo i5 8 GB