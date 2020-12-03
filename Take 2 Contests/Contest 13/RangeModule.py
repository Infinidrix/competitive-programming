class Tree:
    def __init__(self, val):
        self.val = val
        self.filled = False
        self.right = None
        self.left = None


class RangeModule:
    def __init__(self):
        self.root = Tree((0, 2 ** 30))

    def add_range(self, root, left, right):
        
        if root.val[0] == left and root.val[1] == right:
            root.filled = True
            root.left = None
            root.right = None
            return
        mid = root.val[0] + (root.val[1] - root.val[0]) // 2
        
        if not root.left:
            root.left = Tree((root.val[0], mid))
        if not root.right:
            root.right = Tree((mid + 1, root.val[1]))
        
        if left > mid:
            self.add_range(root.right, left, right)
        elif right <= mid:
            self.add_range(root.left, left, right)
        else:
            self.add_range(root.left, left, mid)
            self.add_range(root.right, mid + 1, right)
                
        if root.right.filled and root.left.filled:
            root.filled = True
            root.left = None
            root.right = None
        
    def addRange(self, left: int, right: int) -> None:
        self.add_range(self.root, left, right - 1)

    def query_check(self, root, left, right):
        if not root:
            return False
        if root.val[0] == left and root.val[1] == right:
            return root.filled
        if root.filled:
            return True

        mid = root.val[0] + (root.val[1] - root.val[0]) // 2
        if left > mid:
            return self.query_check(root.right, left, right)
        if right <= mid:
            return self.query_check(root.left, left, right)
        return self.query_check(root.left, left, mid) and self.query_check(root.right, mid + 1, right)
        
    def queryRange(self, left: int, right: int) -> bool:
        return self.query_check(self.root, left, right - 1)

    def remove_range(self, root, left, right):
        if not root:
            return
        
        if root.val[0] == left and root.val[1] == right:
            root.filled = False
            root.right = None
            root.left = None
            return
        
        mid = root.val[0] + (root.val[1] - root.val[0]) // 2
        if not root.left:
            root.left = Tree((root.val[0], mid))
            root.left.filled = root.filled
        if not root.right:
            root.right = Tree((mid + 1, root.val[1]))
            root.right.filled = root.filled
        
        if left > mid:
            self.remove_range(root.right, left, right)
        elif right <= mid:
            self.remove_range(root.left, left, right)
        else:
            self.remove_range(root.left, left, mid) 
            self.remove_range(root.right, mid + 1, right)
        
        if (root.left and root.right and
           root.left.filled and root.right.filled):
            root.filled = True
        else:
            root.filled = False
    
    def removeRange(self, left: int, right: int) -> None:
        self.remove_range(self.root, left, right - 1)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
