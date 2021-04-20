
from linkedlist import LinkedList,Node
from product import Product 
from stack import Stack
from queue import Queue

class OperationToProduct:
  def __init__(self):
    self.linkedList = LinkedList()
    self.AStack = Stack()
    self.AQueue = Queue()

  def case1(self,file):
    try:
      fh = open(file,"r")
      fh.readline()
      #new node
      preNode = Node(None)
      self.linkedList.setStart(None)
      for line in fh:
        arr = list(line.split(","))
        # New product
        product = Product(arr[0],arr[1], float(arr[2]), int(arr[3]))
        node = Node(product)
        #add start
        if (self.linkedList.getStart() is None):
          self.linkedList.setStart(node)
        # connect node        
        preNode.next = node
        preNode = node
      fh.close()
      print("The file is loaded successfully!")
    except:
      print("File-path is not correct!")

  def case2(self):
    try: 
      id = input("Please enter the new product ID:")
      name = input("Please enter the product's name:")
      quantity = int(input("Please enter the product's quantity:"))
      price = float(input("Please enter the product's price:"))
      product = Product(id,name,price,quantity)
      fNode = self.linkedList.start
      # Loop linkedlist => end
      while fNode.next is not None:
        fNode = fNode.next
      node = Node(product)
      fNode.next = node
    except:
      print("Error")
  def case3(self):
    self.linkedList.printProduct()

  def case4(self,file):
    self.linkedList.saveFile(file)
  def case5(self,id):
    product = None
    fNode  = self.linkedList.start
    while fNode is not None:
      #find product by id
      if fNode.product.id == id:
        product = fNode.product
        break
      fNode = fNode.next
    if product is None:
      print("ID is not in the dataset!")
    else:
      print("ID |  Title   | Quantity | Price")
      print(product.id," | ", product.title, " | ", product.quantity , " | ",product.price)
    return product
  def case6(self,id):
    fNode = self.linkedList.start
    product = None
    # Check start
    if (fNode.product.id == id):
      product = fNode.product
      self.linkedList.start = fNode.next
    else:
      # Find product id = id input
      while fNode.next is not None:
        if (fNode.next.product.id == id):
          product = fNode.next.product
          fNode.next = fNode.next.next
          break
        fNode = fNode.next
    if product is not None:
      print("ID |  Title   | Quantity | Price")
      print(product.id," | ", product.title, " | ", product.quantity , " | ",product.price)
      print("The product is removed from the dataset successfully!")
    else:
      print("ID is not in the dataset!")

  def case7(self):
    self.linkedList.sort()

  def generatorBinary(self,n,arr):
    if n > 0:
      arr.append(n%2)
      n = int(n/2)
      return self.generatorBinary(n,arr)
    return arr

  def case8(self,id):
    # Call case 5 return => product
    product = self.case5(id)
    if (product is not None):
      # generator => arr 0,1
      arr = self.generatorBinary(product.quantity,[])
      print("Convert quantity to binary: ","".join(list(map(str,arr)))[::-1]) # convert arr => string => reverse string

  def case9(self,file):
    try:
      fh = open(file,"r")
      fh.readline()
      for line in fh:
        arr = list(line.split(","))
        #New product
        product = Product(arr[0],arr[1], float(arr[2]), int(arr[3]))
        self.AStack.add(product) #Add product      
      fh.close()
      print("ID |  Title   | Quantity | Price")
      # while product is exist => remove and print
      while self.AStack.peek() is not None:
        product = self.AStack.remove()
        print(product.id," | ", product.title, " | ", product.quantity , " | ",product.price)
    except:
      print("File-path is not correct!")

  def case10(self,file):
    try:
      fh = open(file,"r")
      fh.readline()
      for line in fh:
        arr = list(line.split(","))
        #New product
        product = Product(arr[0],arr[1], float(arr[2]), int(arr[3]))
        self.AQueue.add(product)      # Add Queue
      fh.close()
      print("ID |  Title   | Quantity | Price")
      # while product is exist => remove and print
      while self.AQueue.peek() is not None:
        product = self.AQueue.remove()
        print(product.id," | ", product.title, " | ", product.quantity , " | ",product.price)
    except:
      print("File-path is not correct!")
