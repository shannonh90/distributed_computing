#---------------------------------------------------------
# Shannon Hamilton
# shannon@ischool.berkeley.edu
# Homework #3
# September 20, 2016
# hw3test.py
# Test
#---------------------------------------------------------

from hw3.shannon.BST import *
from hw3.shannon import *

T = BSTree()
# T.add("4")
# T.add("2")
# T.add("3")
# T.add("5")
# T.add("1")
# T.add("6")
# 
# T.inOrderPrint()

T.add("hello")
T.add("goodbye")
T.add("paul")
T.add("summer")
T.add("paul")
T.add("goodbye")

T.inOrderPrint()