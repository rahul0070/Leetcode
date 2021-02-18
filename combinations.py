class Solution:
    def __init__(self):
        self.result = []
        self.ki = 0

    def combine(self, n, k):
        
        for i in range(k):
            self.ki = i
            self.run(1, n, i, [], 0)
        return self.result

    def run(self,n1,n2,k, comb, rec):
        print(n1, n2, k, comb, rec)
        if k == 0:
            if len(comb) == self.ki:
                self.result.append(comb)

        else:
            for i in range(n1,n2+1):
                #temp = []
                print('----', i, rec)
                if k-1 <= (n2-i):
                    #temp.append(i)
                    self.run(i+1, n2, k-1, comb+[i], rec+1)
                else:
                    break


if __name__ == '__main__':
    s = Solution()
    n = 4
    k = 3
    print(s.combine(n, k))



