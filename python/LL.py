# python implementation for LinkedList. The code is very similar to geeksforgeeks cause I used that for reference.
# gang-gang
# Credits-> https://www.geeksforgeeks.org/linked-list-set-1-introduction/
 
# Node class
class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data value
        self.next = None  # Initialize next as null or say pointer
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
 
# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
 
    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''
 
    llist.head.next = second; # Link first node with second
 
    '''
    Now next of first Node refers to second.  So they
    both are linked.
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+
    '''
 
    second.next = third; # Link second node with the third node
 
    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+
    '''


# inserting a new node at the beginning-- O(1)T ---- 4 steps
def push(self, New_data):
    new_node = Node(New_data)
    new_node.next = self.head
    self.head = new_node

# Adding a node after a given node-- O(1)T ---- 5 steps
def insertAfter(self, prev_node, new_data):

    # checking if the given prev_node exists
    if (prev_node is None):
        print("the given previous node muyst be in LL")
        return

    # create new node and put the data
    new_node = Node(new_data)

    # make next of new Node as next of prev_node
    new_node.next = prev_node.next

    # make next of prev_node as new_node
    prev_node.next = new_node

# Add a node at the end of the LL-- O(n) ---- 6 steps
# we need to traverse the list becauuse we are adding the node at the end, then change the next of last node to new node.
def append(self, new_data):
    # create a new node, put in the data, set next as None
    new_node = Node(new_data)

    # if the LL is empty, then make the new node as head
    if self.head is None:
        self.head = new_node
        return

    # otherwise we traverse till the last node
    last = self.head
    while(last.next):
        last = last.next

    # change the next of last node
    last.next = new_node
