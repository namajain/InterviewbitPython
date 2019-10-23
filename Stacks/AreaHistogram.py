class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        s = [0]
        m = A[0]
        A.append(-1)
        for i in range(len(A)):

            while s and A[i] < A[s[-1]]:
                t = s.pop()
                m = max(m, A[t] * ((i - s[-1] - 1) if s else i))
            s.append(i)

        return m

s = Solution()
