### implementing a binary tree using node class

class BTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        
    def inorderTraversal(self, root):
        # Left -> Root -> Right
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
    
    def preorderTraversal(self, root):
        # Root -> Left -> Right
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    def postorderTraversal(self, root):
        # Left -> Right -> Root
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res

    def findval(self, searchval):
        if self.data is None:
            print("Empty tree")
            return "Empty Tree"
        if searchval == self.data:
            print(str(self.data) + ' is found')
        elif searchval < self.data:
            # search the left tree
            if self.left is None:
                return "Not found"
            return self.left.findval(searchval)
        elif searchval > self.data:
            # search the right tree
            if self.right is None:
                return "Not found"
            return self.right.findval(searchval)
