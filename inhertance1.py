class a:

    def __init__(self) -> None:
        print('inti in a')

    def feature1(self):
        print('feature 1 is working')

    def feature2(self):
        print('feature 2 is working')


class b:

    def __init__(self) -> None:
        print('inti in b')

    def feature3(self):
        print('feature 3 is working')

    def feature4(self):
        print('feature 4 is working')

class c(b,a):

   def __init__(self) -> None:
       super().__init__()
       print('inti in c')

   def feat(self):
        a1.feature2()

a1 = c()
a1.feat()