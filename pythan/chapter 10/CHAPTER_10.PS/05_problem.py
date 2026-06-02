from random import randint 
class Train:
    
    
     def __init__(self,TrainNo):
         self.TrainNo = TrainNo
     def book(self,fro, to):
         print(f"Ticket is booked in train no:{self.TrainNo} from {fro} to {to}")
     def getstatus(self):
         print(f"Train no:{self.TrainNo} is running on time")
        
        
     def getfare(self,fro,to):
         print(f"Ticket fare in train no: {self.TrainNo} from {fro} to {to} is {randint(222,5555)}") 
          

t = Train(12399)
t.book("Rampur", "Delhi")
t.getstatus()
t.getfare("Rampur", "Delhi")