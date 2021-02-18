class Solution:
    def __init__(self):
        self.result = []
        self.ki = 0
        self.data = {}

    def subsetsWithDup(self, n):
        s = len(n) - 1
        n.sort()
        self.li = n
        for i in range(s+2):
            self.ki = i
            self.run(0, s, i, [])
        return self.result

    def run(self,n1,n2,k,comb):
        if k == 0 and len(comb) == self.ki:
            if tuple(comb) not in self.data:
                self.result.append(comb)
                self.data[tuple(comb)] = 1

        else:
            print(n1, n2)
            for i in range(n1,n2+1):
                if k-1 <= (n2-i): self.run(i+1, n2, k-1, comb+[self.li[i]])
                else: break


s = Solution()
print(s.subsetsWithDup([1,2,2]))