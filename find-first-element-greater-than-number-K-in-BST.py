#Question: Find first element greater than number K in BST

#Source: http://stackoverflow.com/questions/5444394/implementing-binary-search-tree-in-python
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child == None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child == None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)
        
def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)    


def FirstGreaterValue(n,input,greatest):
        #Scenario 1: Node is empty
        if(n is None):
            if (greatest.data > input):
                print(greatest.data)
            else:
                print("Error: No element found")
        #Scenario 2: Node value is GREATER than input
        # Store node data and go LEFT
        elif (n.data > input):
            #handle condition that there is no child node or child node < input
            greatest = n   
            FirstGreaterValue(n.l_child,input,greatest)
        #Scenario 3: Node value is LESS than input, go RIGHT
        elif (int(n.data) <= input):
            FirstGreaterValue(n.r_child,input,greatest)

r = Node(10)
binary_insert(r, Node(8))
binary_insert(r, Node(10))
binary_insert(r, Node(18))
binary_insert(r, Node(15))
binary_insert(r, Node(20))
binary_insert(r, Node(16))
        
input = 16
print ("First value greater than ", input, " is ",end="")
FirstGreaterValue(r,input,r)
 


