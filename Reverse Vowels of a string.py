class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        s=list(s)
        x=['a','e','i','o','u']
        right=len(s)-1
        while left<right:
            if(s[left].lower() in x and s[right].lower() in x):
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            if(s[left].lower() not in x):
                left+=1
            if(s[right].lower() not in x):
                right-=1
            
        s="".join(s)
        return s
        