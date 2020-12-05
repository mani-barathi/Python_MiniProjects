class Stack:
  def __init__(self):
    self.stack=[]  # emty list
    self.top=-1

  def isEmpty(self):
    if len(self.stack)==0:
      return True
    else :
      return False

  def push(self):
    self.top+=1
    element = input("Enter the Element: ")
    self.stack.insert(self.top,element)
    print(f" {element} is pushed")
  
  def pop(self):
    if self.isEmpty():
      print("Stack is empty!")
    else:
      self.top-=1
      print(f"Element poped: {self.stack.pop()}")
  
  def printStack(self):
    if self.isEmpty():
      print("stack is Empty")
    else:
      print(self.stack)

# print(" iniside  main.py: ",__name__)

if __name__=='__main__': 
  s= Stack()  # creating a object of stack
  print("1. push\n2. pop\n3. printStack")  
  while True:
    choice= input("Enter your choice: ")
    if choice=='1':
      Stack.push(s)
    elif choice=='2':
      s.pop()
    elif choice=='3':
      s.printStack()
    else:
      break