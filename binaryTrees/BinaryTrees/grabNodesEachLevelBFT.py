
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg

    #            3
    #          /   \
    #        9      20
    #      /   \    /  \
    #   null  null  15  7

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def levelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            if not root:
                return []

            result = []
            queue = [root]

            while queue:
                level_values = []  # the nodes for each level in the tree get processed in this list
                level_size = len(queue)  # we determine the amount of nodes needed in level_values list by seeing the current length of queue

                for _ in range(level_size):     # for how many nodes we need in that level, perform a BFT traversal to grab the nodes in order
                    current_node = queue.pop(0)
                    level_values.append(current_node.val)

                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)

                result.append(level_values)  # once we got the right amount for that level, append it to a result array, and repeat for the next level

            return result

node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

print("RESULT ---> ", node.levelOrder(node))
