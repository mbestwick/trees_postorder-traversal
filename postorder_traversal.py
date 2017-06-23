"""
Complete the postOrder function in your editor below, which has 1 parameter: a
pointer to the root of a binary tree. It must print the values in the tree's
postorder traversal as a single line of space-separated values.

Input Format
Our hidden tester code passes the root node of a binary tree to your postOrder
function.

Output Format
Print the tree's postorder traversal as a single line of space-separated values.

"""


class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def postOrder(root):
    # base case: if not left and not right
    if not root.left and not root.right:
        print root.data,
    # if just a right node, recursive call on right then print the root
    elif not root.left:
        postOrder(root.right)
        print root.data,
    # if just a left node, recursive call on lfet then print the root
    elif not root.right:
        postOrder(root.left)
        print root.data,
    # if two nodes, recurisve call on left then right then print the root
    else:
        postOrder(root.left)
        postOrder(root.right)
        print root.data,
