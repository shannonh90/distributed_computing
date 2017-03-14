#---------------------------------------------------------
# Shannon Hamilton
# shannon@ischool.berkeley.edu
# Homework #3
# September 20, 2016
# hw3.py
# Main
#---------------------------------------------------------

#After work is loaded into dictionary, program should run a main loop that takes
# as input a test word, and finds if it is in the bST. for should look like this:
# Query?  elizabeth 
# The word elizabeth appears XXX times in the tree

#If the key word "stats" is given, the program should print out the number of 
#entries in the tree (SIZE) and the maximum depth of the tree (HEIGHT). 

#if the key word "terminate" is given, the program should terminate. 


from hw3.shannon.BST.py import *
#not sure if I have to change file name like I did above?

def read_file(filename):
    with open(filename, 'rU') as document:
        text = document.read()
    filter_punc = lambda t: ''.join([x.lower() for x in t if x.isalpha()])
    words = [x for x in map(filter_punc, text.split()) if x]
    return words


def main():
    while(True):
        print("Enter the file name to read:")
        filename = input('> ')
        try:
            words = read_file(filename)
        except IOError:
            print("Unable to find the file {}".format(filename))
        else:
            tree = BSTree()
            for word in words:
                tree.add(word)
            break

    ######################
    # Begin Student Code #
    ######################
    #Functions for use
    # tree.add(word)
    # tree.find(word)
    # tree.size()
    # tree.height()
    # tree.inOrderPrint()


if __name__ == "__main__":
    main()