class BSTree:
  def __init__(self,person):
    self.left = None
    self.right  = None
    self.person = person


  def insert(self,person):
    #  Check value ID
    if self.person:
      # Left
      if person.ID < self.person.ID:
        if self.left is None:
          self.left = BSTree(person)
        else:
          self.left.insert(person)
     #  Right
      elif person.ID > self.person.ID:
        if self.right is None:
          self.right = BSTree(person)
        else:
          self.right.insert(person)
    else:
      # Center
      self.person = person
  # Left to Right
  def Inorder(self,root):
    res = []
    if root:
      res = self.Inorder(root.left)
      res.append(root.person)
      res = res + self.Inorder(root.right)
    return res
    
      # Pre
      # res.append(root.data)
      # res = res + self.PreorderTraversal(root.left)
      # res = res + self.PreorderTraversal(root.right)
      # Post
      # res = self.PostorderTraversal(root.left)
      # res = res + self.PostorderTraversal(root.right)
      # res.append(root.data)
  
  def findPerson(self,ID):
    if ID < self.person.ID:
      # Find Left
      if self.left is None:
        return None
      return self.left.findPerson(ID)
      # FindRight
    elif ID > self.person.ID:
      if self.right is None:
        return None
      return self.right.findPerson(ID)
    else:
      return self.person

  # Loop to last left
  def minValueNode(self,node):
    current = node
    while current.left is not None:
      current = current.left
    return current

  def delete(self,root,ID):
    if root is None:
      return root
    if ID < root.person.ID:
      #  Try left
      root.left = self.delete(root.left,ID)
    elif ID > root.person.ID:
      # Try right
      root.right = self.delete(root.right,ID)
    else:
      # Check Left
      if root.left is None:
        temp = root.right
        root  = None
        return temp
      # Check right
      elif root.right is None:
        temp = root.left 
        root = None
        return temp
      temp = self.minValueNode(root.right)
      root.person = temp.person
      root.right = self.delete(root.right,temp.person.ID)
    return root    