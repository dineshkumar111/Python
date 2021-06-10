

class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu 
        self.ram=ram

    def config(self):
        print("configuration is :",self.cpu,self.ram)

        


c1 =computer('i5','8gb')
c2 =computer('Ryzen 3',"8gb")

c1.config()
c2.config()