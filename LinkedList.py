class node :
	"""docstring for node"""
	def __init__(self, data=None):
		self.data=data
		self.next=None
		
class linked_list:
	"""docstring for linked_list
	The linked list must have a node always. 
	The head node is created automatically and is not accessed by the user.
	"""
	def __init__(self):
		self.head = node()
	
	# Add an element to the linked list 
	def append(self, data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:  # till the next element of the current node is not equal to null
			cur=cur.next
		cur.next=new_node

	def length(self):
		cur=self.head
		total_nodes=0
		while cur.next!=None:
			total_nodes+=1
			cur=cur.next
		return total_nodes

	def display(self):
		elems=[]
		cur_node=self.head  
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems)

# # testing the list
# my_list=linked_list()   #creating instance of class
# my_list.display()    # calling display function of class
# my_list.append(1)
# my_list.append(2)
# my_list.display()

	def get(self,index):
		if(index>=self.length() or index<=0):
			print("Index out of Range.")
			return None
		# Variable for checking the current index we are on
		cur_index=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_index==index:
				return cur_node.data
			else:
				cur_index+=1
# do add the elements first
# x=my_list.get(2)   # Testing the get function 
# print(x)
	
	def erase(self,index):
		if(index>=self.length() or index<=0):
			print("Index out of Range.")
			return None
		cur_index=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_index==index:
				last_node.next=cur_node.next
				return
			else:
				cur_index+=1

		 
