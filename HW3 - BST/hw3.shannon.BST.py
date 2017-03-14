#---------------------------------------------------------
# Shannon Hamilton
# shannon@ischool.berkeley.edu
# Homework #3
# September 20, 2016
# BST.py
# BST
# ---------------------------------------------------------

#Define a new class BST that implements a binary search tree.

#Please design and implement the following methods. 
#Create methods: 
#FIND (RECURSIVE, performs binary search to to see if the word is in the tree, 
	#if so, returns the number of times the word appears in the input text file)
#SIZE (giving number of entries)
#HEIGHT (giving the depth of tree)

#Each node in the tree may keep track of the depth of the current 
#subtree and the number of entries below it


class Node:
    #Constructor Node() creates node
    def __init__(self,word):
        self.word = word
        self.right = None
        self.left = None
        self.count = 1

class BSTree:
    #Constructor BSTree() creates empty tree
    def __init__(self, root=None):
        self.root = root
    
    #These are "external functions" that will be called by your main program - I have given these to you
    
    #Find word in tree
    def find(self, word):
        return _find(self.root, word)
    
    #Add node to tree with word
    def add(self, word):
        if not self.root:
            self.root = Node(word)
            return
        _add(self.root, word)

    #Print in order entire tree
    def in_order_print(self):
        _in_order_print(self.root)

    def size(self):
        return _size(self.root)

    def height(self):
        return _height(self.root)


#These are "internal functions" in the BSTree class - You need to create these!!!

#Function to add node with word as word attribute
def _add(root, word):
    if root.word == word:
        root.count +=1
        return
    if root.word > word:
        if root.left == None:
            root.left = Node(word)
        else:
            _add(root.left, word)
    else:
        if root.right == None:
            root.right = Node(word)
        else:
            _add(root.right, word)
    
#Function to find word in tree
def _find(root, word):
    #YOU FILL THIS IN
    self.placeholder = None #REMOVE

#Get number of nodes in tree
#http://stackoverflow.com/questions/19187901/counting-number-of-nodes-in-a-binary-search-tree
def _size(root):
    count = 0
    if root is not None:
        if root.left is not None:
            count += _size(root.left)
        if root.right is not None:
            count += _size(root.right)
    return count

#Get height of tree
#http://stackoverflow.com/questions/19191707/printing-max-depth-in-binary-search-tree
def _height(root):
    if root == None:
        return 0
    else:
        return max(_height(root.left), _height(root.right))+1
    
#Function to print tree in order
def _in_order_print(root):
    if not root:
        return
    _in_order_print(root.left)
    print(root.word)
    print(root.count)
    _in_order_print(root.right)
