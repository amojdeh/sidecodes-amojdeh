class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i','o', 'u' ]
        
        d = {}
        
        
        st_list = list(s)
        

        
        for i in range(len(st_list)):
            if st_list[i].lower() in vowels:
                d[i] = st_list[i]

            else:
                continue
        j = len(d)-1
        lst = list(d.keys())
        
        for i in range(len(lst)):
            
            st_list[lst[j-i]] = d[lst[i]]
            
        return ''.join(st_list)
        