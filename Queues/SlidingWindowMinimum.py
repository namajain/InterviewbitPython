class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        from collections import deque
        q = deque()
        a = []
        for i in range(B - 1):

            while q and A[i] >= A[q[-1]]:
                q.pop()
            q.append(i)

        for i in range(B - 1, len(A)):

            while q and A[i] >= A[q[-1]]:
                q.pop()
            q.append(i)
            if q[0] < i - B + 1:
                q.popleft()
            a.append(A[q[0]])
        return a
