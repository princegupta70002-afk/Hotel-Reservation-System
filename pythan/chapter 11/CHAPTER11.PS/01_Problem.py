class TwoDvector:
    def __init__(self,i,j):
        self.i = i 
        self.j = j 

    def  show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


a = TwoDvector(2,4)
a.show()
b = ThreeDvector(3,5,2)
b.show()        