class Solution:
    # @param A : tuple of integers
    # @return an integer



    def longestSubsequenceLength(self, A):
        mem = {}
        memd = {}

        def linc( A, i, j):

            if (i, j) in mem:
                pass
            elif j == i:
                return 0
            elif j - i == 1:
                if A[j] > A[i]:
                    mem[i, j] = 1
                else:
                    mem[i, j] = 0
            else:
                mem[i, j] = max([linc(A, i, x) + linc(A, x, j) for x in range(i + 1, j)])
            return mem[i, j]

        def lincd( A, i, j):
            if (i, j) in memd:
                pass
            elif j == i:
                return 0
            elif j - i == 1:
                if A[j] < A[i]:
                    memd[i, j] = 1
                else:
                    memd[i, j] = 0
            else:
                memd[i, j] = max([lincd(A, i, x) + lincd(A, x, j) for x in range(i + 1, j)])
            return memd[i, j]
        j = len(A)
        if j == 0:
            return 0
        if j == 1:
            return 1
        i = 0
        return max([1 + linc(A, i, x) + lincd(A, x, j - 1) for x in range(i, j)])