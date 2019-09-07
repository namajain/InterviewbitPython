# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class MeowError(Exception):
        """Base class for  exceptions"""
        pass
    
class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        
        def meow(ptr):
            if ptr is None:
                return None,None
            x = ptr.val
            ml, Ml = meow(ptr.left)
            mr, Mr = meow(ptr.right)
                
            if Ml is None and mr is None:
                return x,x
            elif Ml is None:
                if mr<=x:
                    raise MeowError
                M=Mr
                m = x
            elif mr is None:
                if Ml >= x:
                    raise MeowError
                m=ml
                M=x
            else:
                if Ml >= x or mr<=x:
                    raise MeowError
                m =ml
                M=Mr
            
            return m,M
        
        try:
            meow(A)
            return 1
        except MeowError:
            return 0

