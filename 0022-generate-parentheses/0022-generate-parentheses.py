class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A = [], left = 0, right = 0):
            if len(A) == 2*n:
                ans.append("".join(A))
                return
            if left < n:
                A.append('(')
                generate(A, left+1, right)
                A.pop()
            if right < left:
                A.append(')')
                generate(A, left, right+1)
                A.pop()

        ans = []
        generate()
        return ans