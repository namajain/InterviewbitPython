class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        a=A.split('/')
        b = []
        for e in a:
            if e in['.','']: continue
            elif e=='..':
                if b: b.pop()
            else: b.append(e)
        return '/'+ '/'.join(b)