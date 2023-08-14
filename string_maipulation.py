## Question1: Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create an empty set to store characters in the current substring
        charset = set()
        
        # Initialize the maximum length of a substring without repeating characters
        res = 0
        
        # Initialize the left pointer for the sliding window
        l = 0
        
        # Loop through the characters of the string using the right pointer (r)
        for r in range(len(s)): 
            # If the current character is already in the set (repeating character)
            while s[r] in charset:
                # Remove the leftmost character from the set
                charset.remove(s[l])
                
                # Move the left pointer to the right to shrink the window
                l += 1
            
            # Add the current character to the set
            charset.add(s[r])
            
            # Calculate the length of the current substring (window) and update the maximum length if needed
            res = max(res, r - l + 1)
        
        # Return the maximum length of a substring without repeating characters
        return res


s = "bbbbdddddafd"
solution = Solution()
output = solution.lengthOfLongestSubstring(s)
print(output)




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
