class vector:
    def __init__(self,l):
      #  self.x , self.y , self.z  = l
        self.l = l    


    # def __add__(self, other):
    #     result = vector(self.x + other.x , self.y + other.y,self.z + other.z)

    #     return result


    # def __mul__(self, other):
    #     result = self.x * other.x + self.y * other.y * self.z * other.z
    #     return result

    # def __str__(self):

    #     return f"vector({self.x} , {self.y} ,{self.z})"




    def __len__(self):
        return 3    

# TEST THE IMPLEMENTATION
v1 = vector([1,2,3])
print(len(v1))