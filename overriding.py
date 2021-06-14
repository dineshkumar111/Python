
class A:

    def show(self):
        print('in A')

class B(A):
    
    def show(self):
        print('in B')


a1 =B()

a1.show()