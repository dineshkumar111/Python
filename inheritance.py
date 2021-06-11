

class a:

    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')


class b(a):

    def feature3(self):
        print('feature 3 is working')

    def feature4(self):
        print('feature 4 is working')

class c(b):

    def feature5(self):
        print('feature 5 is working')

    def feature6(self):
        print('feature 6 is working')


a1 = a()

a1.feature1()
c1 =c()

c1.feature3()


#sample output
#feature 1 is working
#feature 3 is working