class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, a):
        expr = ['+', '-', "*", '/']
        b = []
        for i in a:
            if i not in expr:
                b.append(i)
            else:
                exp = i
                y = b.pop()
                x = b.pop()

                s = x + exp + y
                # print(s)
                b.append(str(eval(s)))
        # print(b)
        return b.pop() 