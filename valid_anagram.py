def valid_anagram(s,t):
    freq_s = [0]*26
    freq_t = [0]*26
    
    for ch in s:
        freq_s[ord(ch)-ord('a')]+=1
    for ch in t:
        freq_t[ord(ch)-ord('a')]+=1
    if freq_t==freq_s:
        return True
    return False

s="anagram"
t="nagaran"
print(valid_anagram(s,t))