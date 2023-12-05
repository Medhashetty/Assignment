Program 1(Easy)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        j = i
        while j >= 0 and s[j] != ' ':
            j -= 1
        return i - j

program 1(medium)

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root
program 2(Hard)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        n = len(s)
        for j in range(n):
            if s[i] == s[n-j-1]:
                i += 1
        if i==n:
            return s
        p = s[i:n][::-1]
        return p + self.shortestPalindrome(s[:i]) + s[i:]