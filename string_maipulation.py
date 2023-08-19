# ## Question1: Given a string s, find the length of the longest substring without repeating characters.

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # Create an empty set to store characters in the current substring
#         charset = set()
        
#         # Initialize the maximum length of a substring without repeating characters
#         res = 0
        
#         # Initialize the left pointer for the sliding window
#         l = 0
        
#         # Loop through the characters of the string using the right pointer (r)
#         for r in range(len(s)): 
#             # If the current character is already in the set (repeating character)
#             while s[r] in charset:
#                 # Remove the leftmost character from the set
#                 charset.remove(s[l])
                
#                 # Move the left pointer to the right to shrink the window
#                 l += 1
            
#             # Add the current character to the set
#             charset.add(s[r])
            
#             # Calculate the length of the current substring (window) and update the maximum length if needed
#             res = max(res, r - l + 1)
        
#         # Return the maximum length of a substring without repeating characters
#         return res


# s = "bbbbdddddafd"
# solution = Solution()
# output = solution.lengthOfLongestSubstring(s)
# print(output)




### ANAGRAM AND PALINDROME


# def is_anagram(word1, word2):
#     return sorted(word1) == sorted(word2)

# def is_palindrome(word):
#     return word == word[::-1]

# def is_anagram_palindrome(word):
#     return is_anagram(word, word[::-1])

# # Example words
# word1 = "listen"
# word2 = "silent"
# palindrome_word = "radar"
# non_palindrome_word = "level"

# # Checking anagrams
# print(f"{word1} and {word2} are anagrams: {is_anagram(word1, word2)}")

# # Checking palindrome
# print(f"{palindrome_word} is a palindrome: {is_palindrome(palindrome_word)}")
# print(f"{non_palindrome_word} is a palindrome: {is_palindrome(non_palindrome_word)}")

# # Checking anagram palindrome
# print(f"{palindrome_word} is an anagram palindrome: {is_anagram_palindrome(palindrome_word)}")
# print(f"{non_palindrome_word} is  an anagram palindrome: {is_anagram_palindrome(non_palindrome_word)}")



# ## To check fro a double string in a list of strings

# def double(letters):

#     n = len(letters)
#     for i in range (n):
#         for j in range(i + 1, n):
#             if letters[i] == letters[j]:
#                 print(i, letters[i], "is double") and i !=j


# letters = ['s', 'u', 'n', 'd', 'a', 'y', 's', 'u']
# print(double(letters))

# Question on: longest substring with at most two distinct characters

# class Solution:
#     def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
#         charset = {}          # A dictionary to store character frequencies
#         distinct_count = 0    # Count of distinct characters
#         res = 0               # Length of the longest substring
#         l = 0                 # Left pointer of the sliding window
#         n = len(s)            # Length of the string
        
#         for r in range(n):    # Loop through characters using the right pointer (r)
#             if s[r] not in charset:
#                 distinct_count += 1
#                 charset[s[r]] = 0   # Initialize count for the new character
            
#             charset[s[r]] += 1      # Increase character count
            
#             # Check if there are more than two distinct characters
#             while distinct_count > 2:
#                 charset[s[l]] -= 1      # Decrease count of leftmost character
#                 if charset[s[l]] == 0:
#                     distinct_count -= 1  # Reduce distinct count if count becomes zero
#                     del charset[s[l]]    # Remove character from dictionary
#                 l += 1                  # Move the left pointer to shrink the window
            
#             res = max(res, r - l + 1)  # Update maximum length
            
#         return res  # Return the length of the longest substring

# s = "egbowanuchiogormu"
# solution = Solution()
# output = solution.lengthOfLongestSubstringTwoDistinct(s)
# print(output)



# # QUESTION:  Longest Palindromic Substring
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)  # Length of the input string
#         dp = [[False] * n for _ in range(n)]  # Create a 2D table to store whether substrings are palindromes
#         start = 0  # Initialize the starting index of the longest palindrome substring
#         max_length = 1  # Initialize the length of the longest palindrome substring
        
#         # Mark single characters as palindromes (base case)
#         for i in range(n):
#             dp[i][i] = True
        
#         # Loop through all possible substring lengths
#         for length in range(2, n + 1):
#             for i in range(n - length + 1):
#                 j = i + length - 1
#                 # Check if characters at the two ends are the same
#                 if s[i] == s[j]:
#                     # If the substring between them is a palindrome (or if it's of length 2)
#                     if length == 2 or dp[i + 1][j - 1]:
#                         dp[i][j] = True
#                         # Update the longest palindrome substring if needed
#                         if length > max_length:
#                             start = i
#                             max_length = length
        
#         # Return the longest palindrome substring found
#         return s[start:start + max_length]

