class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        
        for i in range(left,right+1):
            if '0' in str(i):
                continue
            else:
                c = 0
                for j in str(i):
                    if i % int(j) != 0:
                        break
                    else:
                        c += 1
                        if c == len(str(i)):
                            ans.append(i)
        return ans
                