class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        I = { 'val': 1, 'name':'I'}
        IV = { 'val': 4, 'name':'IV'}
        V = { 'val': 5, 'name':'V'}
        IX = { 'val': 9, 'name':'IX'}
        X = { 'val': 10, 'name':'X'}
        XL = { 'val': 40, 'name':'XL'}
        L = { 'val': 50, 'name':'L'}
        XC = { 'val': 90, 'name':'XC'}
        C = { 'val': 100, 'name':'C'}
        CD = { 'val': 400, 'name':'CD'}
        D = { 'val': 500, 'name':'D'}
        CM = { 'val': 900, 'name':'CM'}
        M = { 'val': 1000, 'name':'M'}
        digits = [M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, I]
        vector = []

        for d in digits:
            vector.extend([d['name'] for i in range(A//d['val'])])
            A = A%d['val']
        return ''.join(vector)
s= Solution()
print(s.intToRoman(49))