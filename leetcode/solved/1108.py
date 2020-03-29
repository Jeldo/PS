class Solution:
    def defangIPaddr(self, addr):
        return addr.replace('.','[.]')


sol = Solution()
print(sol.defangIPaddr('1.255.244.233'))