'''
Question: Find the Lowest (nearest/first) Common Ancestor (LCA) of two nodes in a binary tree
          Each node had parent, left and right node(s)  
           
Algorithm: :bulb: :rocket:
0. Traverse up from given nodes to root to find the level of each node
1. if nodes are not at the same level, keep moving the deepest node (closer to the root) until the level of both given nodes are equal
2. Move each node close to the root until parents are same!
 
'''
