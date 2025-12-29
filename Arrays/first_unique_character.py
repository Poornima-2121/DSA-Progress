def first_unique_character(s):
    freq = [0]*26
    
    for ch in s:
        freq[ord(ch)-ord('a')] += 1

    for i in range(len(s)):
        if freq[ord(s[i])-ord('a')] == 1:
            return i

    return -1


print(first_unique_character("leetcode"))
print(first_unique_character("loveleetcode"))
print(first_unique_character("aabb"))
