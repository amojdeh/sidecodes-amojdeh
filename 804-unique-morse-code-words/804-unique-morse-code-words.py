import string as st
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l = []
        for word in words:
            
            new = ''
            for j in word:
                new += morse[st.ascii_lowercase.index(j)]
            l.append(new)
            
        return len(set(l))