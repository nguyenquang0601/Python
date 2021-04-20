from operationtoproduct import OperationToProduct

class AS2_Main:
  def run(self):
    option = -1
    operation = OperationToProduct()
    file = ""
    while option != 0:
      print("""
+-------------------Menu------------------+

1. Load data from file and display

2. Input & add to the end.

3. Display data

4. Save product list to file.

5. Search by ID

6. Delete by ID

7. Sort by ID.

8. Convert to Binary 

9. Load to stack and display

10. Load to queue and display.

Exit:

0. Exit

+-----------------------------------------.+

""")

      option = int(input("Enter Option:"))
      if (option == 1):
        print("Choice 1: Load data from file and display")
        file = input("Please enter the find path:")
        operation.case1(file)
      if (option == 2):
        print("Choice 2: Input & add to the end")
        operation.case2()
      if (option == 3):
        print("Choice 3: Display data")
        operation.case3()
      if (option == 4):
        print("Choice 4: Save product list to file")
        file_output  = input("Please enter the output path:")
        operation.case4(file_output)
        print("The file is saved successfully!")
      if (option == 5):
        print("Choice 5: Search by ID")
        id = input("Please enter the ID: ")
        operation.case5(id)
      if (option == 6):
        print("Choice 6: Deleted by ID")
        id = input("Please enter the ID: ")
        operation.case6(id)
      if (option == 7):
        print("Choice 7: Sorted by ID")
        operation.case7()
      if (option == 8):
        print("Choice 8: Convert to Binary")
        id = input("Please enter the ID: ")
        operation.case8(id)
      if (option == 9):
        print("Choice 9: Load to stack and display")
        operation.case9(file)
      if (option == 10):
        print("Choice 10: Load to queue and display")
        operation.case10(file)
      

if __name__ == "__main__":
  main = AS2_Main()
  main.run()