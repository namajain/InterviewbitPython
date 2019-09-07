class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        iEntry = {}
        iMap = {}
        for i in A:

            l = True if i - 1 in iMap else False
            r = True if i + 1 in iMap else False
            if l and r:
                tm, mt = (iMap[i - 1], iMap[i + 1]) if len(iEntry[iMap[i + 1]]) > len(iEntry[iMap[i - 1]]) else (iMap[i + 1], iMap[i - 1])

                iMap[i] = tm
                iEntry[tm].append(i)
                iEntry[mt].extend(iEntry[tm])

                for e in iEntry[tm]:
                    iMap[e] = mt

                del iEntry[tm]
            elif l:
                iMap[i] = iMap[i - 1]
                iEntry[iMap[i]].append(i)
            elif r:
                iMap[i] = iMap[i + 1]
                iEntry[iMap[i]].append(i)
            else:
                iMap[i] = i
                iEntry[i] = [i]
        m = 0
        for i in iEntry.values():
            if len(i) > m:
                m = len(i)
        return m
#
# s = Solution()
# s.longestConsecutive([100, 4, 200, 1, 3, 2 ])

