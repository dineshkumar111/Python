

class vss:

    def execute(self):
        print("Compling")
        print("Running")
        
class myeditor:

    def execute(self):
        print('Spell check')
        print('convection check')
        print("Compling")
        print("Running")


class laptop:

    def code(self,ide):
        ide.execute()


ide = vss()
lap1 = laptop()

lap1.code(ide)


ide = myeditor()
lap1 = laptop()

lap1.code(ide)


#sample output
#Compling
#Running
#Spell check
#convection check
#Compling
#Running




    
