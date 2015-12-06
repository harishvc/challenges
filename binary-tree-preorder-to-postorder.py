#Reference:http://stackoverflow.com/questions/4537969/pre-order-to-post-order-traversal

'''
Given preorder construct postorder
'''

#Generate postorder from preorder
def postorder(preorder):
    if not preorder:
        return []
    else:
        root = preorder[0]
        left = preorder[1: int(len(preorder)/2)+1]
        right = preorder[len(left) + 1:]
        return postorder(left) + postorder(right) + [root]

if __name__ == '__main__':
    preorder = [20, 10, 6, 15, 30, 35]
    print("preorder >>>", preorder)
    print("postorder >>>", postorder(preorder))
