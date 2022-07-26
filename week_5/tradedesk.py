# Time Complexity -O(n)
# Space Cpmplexity-O(1)
def solution(pattern, s):
    # Helper functions
    def isVowel(c):
        if(c == 'a'or c == 'e'or c == 'i'or c == 'o'or c == 'u' ):
            return True
        else:
            return False
    def isConstant(c):
        if not isVowel(c):
            return True
        else:
            return False
            
    # vowels=0
    # constants=1
    
    # edge case 1 -> pattern longer than string
    if len(pattern) >=len(s):
        return 0
    
    s=list(s)
    pattern=list(pattern)
    for i,v in enumerate(s):
        if isVowel(v):
            s[i]="0"
        elif isConstant(v):
            s[i]="1"
    n=len(pattern)
    matching =0
    for i in range(len(s)):
        substring=s[i:i+n]
        # print (substring)
        # print(pattern)
        if s[i:i+n]==pattern:
            matching+=1
    return matching
            
if __name__=="__main__":      
    pattern = "010"  
    s = "amazing"
    print(solution(pattern, s))
    
    
    
    
    