from Operation import Operation 
class Main:
  def run(self):
    option = -1
    operation = Operation()
    while option != 0:
      print("""+-------------------Menu------------------+

Person Tree:

1. Load the data from the file.

2. Insert a new Person.

3. Inorder traverse

4. Breadth-First Traversal traverse

5. Search by Person ID

6. Delete by Person ID

Exit:

0. Exit

+-----------------------------------------.+

""")
      option = int(input("Enter Option:"))
      if option == 1:
        print("Choice 1: Load data from file and display")
        file = input("Please enter the find path:")
        operation.loadFile(file)       
      if option == 2:
        print("Choice 2: Insert a new Person")
        operation.addNewPerson()

      if option == 3: 
        print("Choice 3: Inorder traverse")
        operation.InorderTraverse()
      if option == 4:
        print("Choice 4: Breadth-First Traversal traverse")
        operation.Bfs()
      if option == 5:
        print("Choice 5: Search by Person ID")
        ID = input("Please insert the ID:")
        operation.SearchbyID(ID)
      if option == 6:
        print("Choice 6: Delete by Person ID")
        ID = input("Delete the person with the ID =")
        operation.DeleteByID(ID)
  

if __name__=="__main__":
  IMain = Main()
  IMain.run() 