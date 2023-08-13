## Question1: Given a string s, find the length of the longest substring without repeating characters.

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



## To check fro a double string in a list of strings

def double(letters):

    n = len(letters)
    for i in range (n):
        for j in range(i + 1, n):
            if letters[i] == letters[j]:
                print(i, letters[i], "is double") and i !=j


letters = ['s', 'u', 'n', 'd', 'a', 'y', 's', 'u']
print(double(letters))
