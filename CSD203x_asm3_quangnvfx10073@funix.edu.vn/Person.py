class Person:
  def __init__(self,ID,Name,Day,Birthplace):
    self.ID = ID
    self.Name = Name
    self.DayofBirth = Day
    self.Birthplace = Birthplace
  def printDetail(self):
    print(self.ID," ", self.Name," ",self.DayofBirth," ", self.Birthplace )