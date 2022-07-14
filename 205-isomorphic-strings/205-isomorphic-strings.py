class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = {}
        if len(set(list(s))) != len(set(list(t))):
            return False
        for i in range(len(s)):
            if s[i] not in sd:
                sd[s[i]] = t[i]
            else:
                if t[i] == sd[s[i]]:
                    continue
                else:
                    return False
        return True
#         for i in s:
#             if i in sd:
#                 sd[i] += 1
#             else:
#                 sd[i] = 1
#         for i in t:
#             if i in st:
#                 st[i] += 1
#             else:
#                 st[i] = 1
                
#         if list(sd.values()) != list(st.values()):
#             return False
#         else:
         
        