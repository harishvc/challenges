#Question: Find if an element exists in BST

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

#http://www.laurentluce.com/posts/binary-search-tree-library-in-python/
def binary_lookup(data, node):
        if data < node.data:
            if node.l_child is None:
                return None, None
                return "Not Found!"
            return binary_lookup(data, node.l_child)
        elif data > node.data:
            if node.r_child is None:
                #return None, None
                return "Not Found!"
            return binary_lookup(data, node.r_child)
        else:
            #return self, parent
            return "Found!!!"
        
def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print(root.data, end=", ")
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)    


r = Node(10)
binary_insert(r, Node(8))
binary_insert(r, Node(10))
binary_insert(r, Node(18))
binary_insert(r, Node(15))
binary_insert(r, Node(20))
binary_insert(r, Node(16))

print("Elements (in-order): ", end="")
in_order_print(r)

#print("pre order")
#pre_order_print(r)

print (" ")
FIND = 5
print("Looking for ", FIND, ": ",binary_lookup(FIND,r))

FIND = 20
print("Looking for ", FIND, ": ",binary_lookup(FIND,r))
