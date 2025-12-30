## Two Sum
**Approach:**
- Use a hashmap to store numbers and their indices.
- For each number, check if its complement exists.
**Time Complexity:** O(n)  
**Space Complexity:** O(n)

## First Unique Character in a String
**Approach:**
- Use a frequency array of size 26 to count characters.
- Traverse the string again to find the first character with frequency 1.
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## Valid Anagram
**Approach:**
- Count the frequency of each character in both strings using fixed-size arrays.
- If both frequency arrays are equal, the strings are anagrams.
**Time Complexity:** O(n)
**Space Complexity:** O(1)

## Longest Substring without repeating characters
**Approach**
- Use a sliding window with two pointers and a set.
- Expand the window using the right pointer.
- If a duplicate is found, shrink the window from the left until it’s removed.
- Track the maximum window size.
**Time Complexity:** O(n) — each character is added and removed at most once
**Space Complexity:** O(min(n, charset)) → effectively O(1)
