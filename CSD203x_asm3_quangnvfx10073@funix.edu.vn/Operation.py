#Import Class
from BST import BSTree
from Person import Person
from Queue import Queue

class Operation:
  def __init__(self):
    self.IBSTree =  BSTree(None)
    self.IQueue = Queue()
  # Load file to data set
  def loadFile(self,file): 
    try:
      fh = open(file,"r")
      fh.readline()
      for line in fh:
        arr = list(line.rstrip().split(','))
        # New person
        person = Person(arr[0],arr[1],arr[2],arr[3])
        #  Add person to Tree
        self.IBSTree.insert(person)
      print("The file is loaded successfully!")
    except:
      print("File path is correct!")
  # Add person to dataset
  def addNewPerson(self):
    IDExist = True
    ID = None
    while IDExist:
      ID = input("Please insert the new ID:")
      #  Check ID is existed
      person = self.IBSTree.findPerson(ID)
      if person is None:
        IDExist = False
      else:
        print("This ID has been chosen, please choose anothor ID!")
    name = input("Please insert the Name:")
    birthplace = input("Please insert the Birthplace:")
    birthofDate = input("Please insert the Birth of Date:")
    person = Person(ID,name,birthofDate,birthplace)
    # Add to Tree
    self.IBSTree.insert(person)
    print("New ID:", person.ID)
    print("Name:", person.Name)
    print("Birthplace:",person.Birthplace)
    print("Date of birth:",person.DayofBirth)
    input("Please tyoe anything to come back to the main memu")

  # Inorder : Left to Right

  def InorderTraverse(self):
    lists = self.IBSTree.Inorder(self.IBSTree)
    print("ID | Name | Day of Birth | Birthplace")
    for person in lists:
      person.printDetail()
    input("Please tyoe anything to come back to the main memu")
  
  # Queue
  def Bfs(self):
    print("ID | Name | Day of Birth | Birthplace")
    if self.IBSTree is None:
      return 
    self.IQueue.add(self.IBSTree)
    # Loop Queue and Print
    while self.IQueue.peek() is not None:
      current_node = self.IQueue.remove()
      current_node.person.printDetail()
      if (current_node.left is not None):
        self.IQueue.add(current_node.left)
      if (current_node.right is not None):
        self.IQueue.add(current_node.right)
    input("Please tyoe anything to come back to the main memu")
  
  # Search Person
  def SearchbyID(self,ID):
    print("Search for ID = ",ID)
    person = self.IBSTree.findPerson(ID)
    if person is not None:
      print("ID | Name | Day of Birth | Birthplace")
      person.printDetail()
    else:
      print("The searched ID is not valid")
    input("Please tyoe anything to come back to the main memu")
  
  # Delete by ID
  def DeleteByID(self,ID):
    #Search Person
    personFound =  self.IBSTree.findPerson(ID)
    if personFound is not None:
      # Delete Person
      self.IBSTree.delete(self.IBSTree,ID)
      print("ID | Name | Day of Birth | Birthplace")
      personFound.printDetail()
    else:
      print("The searched ID is not valid")
    input("Please tyoe anything to come back to the main memu")