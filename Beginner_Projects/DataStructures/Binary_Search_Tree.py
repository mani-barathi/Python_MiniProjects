SPACE = 5
class TreeNode:
	def __init__(self,value=0):
		self.value = value
		self.left = None
		self.right = None

	def __repr__(self):
		return f'{self.value}'

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def __repr__(self):
		self.printTree(self.root,SPACE)

	def isEmpty(self):
		if self.root is not None:
			return False
		return True

	def height(self,node):
		if node:
			left_height = self.height(node.left)
			right_height = self.height(node.right)
			if left_height > right_height:
				return left_height + 1
			else:
				return right_height + 1
		return -1							# if it is None return -1

	def printTree(self,current_node,new_space):
			# right -->   
		#center -->
			# left -->
		if current_node:
			new_space += SPACE
			self.printTree(current_node.right,new_space)
			print()
			for i in range(SPACE,new_space):
				print(" ",end='')
			print(current_node.value)
			self.printTree(current_node.left, new_space)

	def preOrderTraversal(self,node):	# root left right
		if node:
			print(node.value,end=' ')
			self.preOrderTraversal(node.left)
			self.preOrderTraversal(node.right)

	def inOrderTraversal(self,node):	# left root right
		if node:
			self.inOrderTraversal(node.left)
			print(node.value,end=' ')
			self.inOrderTraversal(node.right)

	def postOrderTraversal(self,node):	# left right root
		if node:
			self.postOrderTraversal(node.left)
			self.postOrderTraversal(node.right)
			print(node.value,end=' ')

	def insertNode(self,new_node):
		if self.isEmpty():
			self.root = new_node
			print(f'{new_node.value} is added as a Root Node')
		else:
			temp = self.root
			while temp:
				if temp.value == new_node.value:
					print('No new duplicates allowed')
					return
				elif new_node.value < temp.value:
					if temp.left is None:
						temp.left = new_node
						print(f'{new_node.value} is added at left Tree')
						return
					temp = temp.left

				elif new_node.value > temp.value:
					if temp.right is None:
						temp.right = new_node
						print(f'{new_node.value} is added right Tree')
						return
					temp = temp.right
	
	def deleteHandler(self,item):
		 if self.root:
		 	if self.root.value == item :       # if the item is root node
		 		if self.height(self.root) == 0:
		 			temp = self.root
		 			self.root = None
		 		else:
		 			self.root = self.deleteNode(self.root,item)
		 			temp = self.root
		 	
		 	else: 
		 		temp = self.deleteNode(self.root,item)
		 	print(f'returned Temp: {temp}')
		 	return temp


	def deleteNode(self,current_node,item):
		# delete leaf node
		# delete a node with one child
		# delete a node with two child
		if current_node is None:
			return current_node

		elif item < current_node.value:
			current_node.left = self.deleteNode(current_node.left,item)

		elif item > current_node.value:
			current_node.right = self.deleteNode(current_node.right,item)

		else:			# when item == current_node.value
			if current_node.left is None:    # node with only right child or No child
				temp = current_node.right
				del current_node
				return temp

			elif current_node.right is None:  # node with only left child
				temp = current_node.left
				del current_node
				return temp

			else:		# node with two children
				temp = self.minValueNode(current_node.right)
				current_node.value = temp.value
				current_node.right = self.deleteNode(current_node.right,temp.value)

		return current_node


	def minValueNode(self,current_node):
		min_node = current_node
		while min_node.left:
			min_node = min_node.left
		return min_node

	def searchNode(self,item):
		if self.root :
			temp = self.root
			while temp:
				if item == temp.value:
					return temp
				elif item < temp.value:
					temp = temp.left
				else:
					temp = temp.right
			return temp

	def breadthFirstSearch(self):
		if self.root:
			queue = [self.root]
			while queue:
				current = queue.pop(0)
				print(current.value,end=' ')
				if current.left:
					queue.append(current.left)
				if current.right:
					queue.append(current.right)
			print()

	def depthFirstSearch(self):
		if self.root:
			stack = [self.root]
			while stack:
				current = stack.pop()
				print(current.value,end=' ')
				if current.right:
					stack.append(current.right)
				if current.left:
					stack.append(current.left)
			print()
	
def main():
	bst = BinarySearchTree()
	
	print("1. Insert Node")
	print("2. Search Node")
	print("3. Delete Node")
	print("4. Print Node")
	print("5. Pre/In/Post Order Traversal")
	print("6. Tree Heigth")
	print("7. BFS/DFS")
	print("0. Exit ")
	while True:
		choice = int(input("\nWhat do you  want to do: "))
		if choice == 1:
			print('INSERT MODE')
			value = int(input("Enter the value of the Node: "))
			new_node = TreeNode(value)
			bst.insertNode(new_node)
		elif choice == 2:
			print('SEARCH MODE')
			value = int(input("Enter the value of the Node: "))
			result = bst.searchNode(value)
			if result:
				print(result.value,'is present in the Tree')
			else:
				print(value,'is not present in the Tree')

		elif choice == 3:
			print(" DELETE MODE")
			value = int(input("Enter the value of the Node to be deleted: "))
			is_present = bst.searchNode(value) 
			if is_present :
				result = bst.deleteHandler(value)
				print(f'result: {result}')
				print(f'Node deleted from the Tree')
			else:
				print(f'{value} is not present in the Tree')

		elif choice == 4:
			print('PRINT MODE')
			result = bst.printTree(bst.root,SPACE)
			print()

		elif choice == 5:
			print('TRAVERSAL MODE')
			print('PreOrder: ',end='')
			bst.preOrderTraversal(bst.root)
			print('\nInOrder : ',end='')
			bst.inOrderTraversal(bst.root)
			print('\nPostOrder: ',end='')
			bst.postOrderTraversal(bst.root)
			print()

		elif choice == 6:
			print('TREE HEIGHT')	
			print('Height:',bst.height(bst.root))

		elif choice == 7:
			print('BFS: ',end='')	
			bst.breadthFirstSearch()
			print('DFS: ',end='')	
			bst.depthFirstSearch()

		elif choice == 0:
			print('Exit')
			break

if __name__ == '__main__':
	main()