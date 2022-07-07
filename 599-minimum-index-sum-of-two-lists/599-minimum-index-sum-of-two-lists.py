class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = {}
        
        for i in list1:
            if i in list2:
                ans[i] = list1.index(i) + list2.index(i)
    
        
        if len(ans) == 1:
            return ans.keys()
        key_list = list(ans.keys())
        value_list = list(ans.values())
        ind = []
        for i in range(len(value_list)):
            if value_list[i] == min(value_list):
                ind.append(key_list[i])
                
        return ind