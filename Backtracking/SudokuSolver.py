class Solution:
    # @param A : list of list of chars
    # @return nothing

    def solveSudoku(self, A):
        eligibleSet = {str(s) for s in range(1, 10)}
        ilim = 8
        jlim = 8
        a = [list(r) for r in A]
        def fillOptions(i, j):
            qi = i // 3 * 3
            qj = j // 3 * 3

            ans = eligibleSet - set(a[i])
            # #print('ans 1 ' + ans.__str__())
            ans = ans - set([r[j] for r in a])
            # #print('ans 2 ' + ans.__str__())
            ans = ans - set([x for r in a[qi:qi + 3] for x in r[qj:qj + 3]])
            #print('ans ' + ans.__str__())
            return ans

        def solve(i, j):
            nonlocal a
            #print ('at '+str(i) +' '+ str(j))
            if a[i][j] == '.':

                opts = fillOptions(i, j)
                for opt in opts:
                    #print('trying '+opt)
                    a[i][j]=opt
                    if not checkAndSolve(i, j):
                        a[i][j] = '.'
                    else:
                        return True
            else:
                return checkAndSolve(i, j)

        def checkAndSolve(i, j):
            if j < jlim:
                return solve(i, j + 1)
            elif i < ilim:
                return solve(i + 1, 0)
            else:
                #print(a)
                return True

        solve(0, 0)
        return a

# s = Solution()
# ans = s.solveSudoku([ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ])
#print(ans)