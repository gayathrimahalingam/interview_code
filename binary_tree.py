### implementing a binary tree using node class

class BTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.parent = None

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

def createMinimalBST(array):
    return createMinimalBSTree(array, 0, len(array)-1)

def createMinimalBSTree(array, start, end):
    if end < start:
        return None
    
    mid = (start + end) / 2
    n = BTree(array[mid])
    n.left = createMinimalBSTree(array, start, mid-1)
    n.right = createMinimalBSTree(array, mid+1, end)
    return n

def printTree(root):
    if root is None:
        return
    elif root.left is None and root.right is None:
        print(root.data)
        return
    else:
        print(root.data)
        printTree(root.left)
        printTree(root.right)
        return

if __name__=="__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    tree_root = createMinimalBST(array)
    #printTree(tree_root)
    res = tree_root.inorderTraversal(tree_root)
    print(res)
    res = tree_root.preorderTraversal(tree_root)
    print(res)
