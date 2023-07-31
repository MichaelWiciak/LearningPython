class BinaryTree(object):
    
    def __init__(self, root, givenWholeTree = False):
        if givenWholeTree:
            self._root=root[0]
            self._leftTree = BinaryTree(root[1], isinstance(root[1], list)) if root[1]!=None else None
            self._rightTree = BinaryTree(root[2], isinstance(root[2], list)) if root[2]!=None else None
        else:
            self._root = root
            self._leftTree = None
            self._rightTree = None
        
    def getRoot(self):
        return self._root
    
    def getLeftChild(self):
        return self._leftTree
    
    def getRightChild(self):
        return self._rightTree
    
    def setLeftChild(self, leftTree):
        if isinstance(leftTree, BinaryTree):
            self._leftTree = leftTree
        else:
            raise TypeError('setLeftChild method takes a BinaryTree')
            
    def setRightChild(self, rightTree):
        if isinstance(rightTree, BinaryTree):
            self._rightTree = rightTree
        else:
            raise TypeError('setRightChild method takes a BinaryTree')    
            
    def __insertValue(self, value):
        if value.getRoot()>self.getRoot():
            #insert on the right
            if self.getRightChild() == None:
                self.setRightChild(value)
            else:
                self.getRightChild().__insertValue(value)
        else:
            #insert on the left
            if self.getLeftChild() == None:
                self.setLeftChild(value)
            else:
                self.getLeftChild().__insertValue(value)
                
    def insert(self, value):
        self.__insertValue(BinaryTree(value))
        
    def search(self, value):
        if self._root == value:
            return True
        if self._rightTree!=None:
            if value>self._root:
                return self._rightTree.search(value)
        if self._leftTree!=None:
            if value<self._root:
                return self._leftTree.search(value)
        return False
