class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        
        def dictize(s):
            d={}
            for i in s:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
            return d
        
        n=len(s)
        np=len(p)
        d=dictize(p)
        dp=dictize(s[0:np])
        ans=[]
        if dp==d:
            ans.append(0)
        for i in range(n-np):
            
            dp[s[i]]-=1
            if dp[s[i]]==0:
                del dp[s[i]]
            if s[i+np] in dp:
                dp[s[i+np]]+=1
            else:
                dp[s[i+np]]=1
            if dp==d:
                ans.append(i+1)
        return ans