from abc import ABC,abstractclassmethod, abstractmethod

class computer(ABC):

    @abstractmethod
    def process(self):
        pass

class whiteboard(computer):

    def write(self):
        print('its writing')

class laptop(computer):

    def process(self):
        print('its working')

class programmer:

    def work(self,com):
        print('solving bugs')
        com1.process()


com1=laptop()
prog1=programmer()
prog1.work(com1)



