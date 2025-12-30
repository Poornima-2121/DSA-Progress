def longest_substring_without_repeating_chars(s):
    left=0
    right=0
    chars = set()
    cnt=0
    while right<len(s):
        while s[right] in chars:
            chars.remove(s[left])
            left+=1
        chars.add(s[right])
        right+=1
        cnt = max(cnt, len(chars))
    return cnt
    
testcase1 = "pwwkew"
testcase2 = "abcabcbb"
testcase3 ="bbbbb"
print(longest_substring_without_repeating_chars(testcase1))
print(longest_substring_without_repeating_chars(testcase2))
print(longest_substring_without_repeating_chars(testcase3))