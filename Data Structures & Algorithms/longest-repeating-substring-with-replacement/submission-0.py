class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        w_s = 0
        l = 0
        ans = 0
        freq = {}
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            max_freq = max(max_freq,freq[s[r]])
            w_s = r-l+1

            if w_s-max_freq > k:
                freq[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)
        return ans
            


            

                

