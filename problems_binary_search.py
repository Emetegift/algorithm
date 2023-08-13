
"""
## Question on Binary Search

QUESTION 1: Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, and lays them out face down in a 
sequence on a table. She challenges Bob to pick out the card containing a given 
number by turning over as few cards as possible.
Write a function to help Bob locate the card.
"""

# def locate_card(cards, query):

#     # Create a variable posituin with the value 0
#     position = 0
#     # print('cards:', cards)
#     # print('query:', query)

#     # Set up a loop for repetition
#     # while True:
#     while position < len(cards):
#         # Check if the element at the position match the query
#         if cards[position] == query:
            
#             ## Answer found! return and exit
#             return position
        
#         # Increment the position

#         position +=1

#         # Check if we have reached the end of the array
#         if position == len(cards):
#              ## Number not found, return -1

#             return -1

# Here's how binary search can be applied to our problem:

# def locate_card(cards, query):
#     lo, hi = 0, len(cards) - 1
    
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         mid_number = cards[mid]
        
#         print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
#         if mid_number == query:
#             return mid
#         elif mid_number < query:
#             hi = mid - 1  
#         elif mid_number > query:
#             lo = mid + 1
    
#     return -1




# Binary Search vs. Linear Search

# def locate_card_linear(cards, query):
#     position = 0
#     while position < len(cards):
#         if cards[position] == query:
#             return position
#         position += 1
#     return -1

# tests = {
#     'input': {
#         'cards': list(range(10000000, 0, -1)),
#         'query': 2
#     },
#     'output': 9999998
    
# } 

# # Here is the generic algorithm for binary search, implemented in Python:

# def binary_search(lo, hi, condition):
#     """TODO - add docs"""
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = condition(mid)
#         if result == 'found':
#             return mid
#         elif result == 'left':
#             hi = mid - 1
#         else:
#             lo = mid + 1
#     return -1


# # ## Below is more modified solution to the problem, 
# def locate_card(cards, query):
    
#     def condition(mid):
#         if cards[mid] == query:
#             if mid > 0 and cards[mid-1] == query:
#                 return 'left'
#             else:
#                 return 'found'
#         elif cards[mid] < query:
#             return 'left'
#         else:
#             return 'right'
    
#     return binary_search(0, len(cards) - 1, condition)


# testcases

# cards = [13, 11,20, 7, 4, 3, 1, 0]
# query =7
# output = 3

# cards = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
# query =6
# output = 2

# result = locate_card(tests['input']['cards'], tests['input']['query'])
# result=locate_card(cards, query)
# result==output
# print(result)






## The test from line 115 - 126 can also be written as follow;

# The number query occurs somewhere in the middle of the list cards.
# tests = {
#     'input':{    'cards':[13, 11,20, 7, 4, 3, 1, 0],
#         'query':7},
#     'output':3
# }

# tests = {
#     'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
#     'query': 1}, 
#     'output':6
# }


# # query is the first element in cards.
# tests = {
#     'input': {'cards': [4, 2, 1, -1], 
#     'query': 4}, 
#     'output': 0
# }

# query is the last element in cards.
# tests = {
#     'input': {'cards': [3, -1, -9, -127], 
#     'query': -127}, 
#     'output': 3
# }

#  The list cards contains just one element, which is query.
# tests =  {'input': {'cards': [6], 
# 'query': 6}, 
# 'output': 0
# } 

# The list cards does not contain number query.
# tests = {'input': {'cards': [9, 7, 5, 2, -9], 
# 'query': 4}, 
# 'output': -1
# }


# ##  The list cards is empty.
# tests = {'input': {'cards': [], 
# 'query': 7}, 
# 'output': -1
# }


# The list cards contains repeating numbers.
# tests = {
#     'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
#     'query':3},
#     'output': 7
# }

# #  The number query occurs at more than one position in cards.
# tests = {
#     'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 
#     'query': 6},

#     'output': 2
# }


# result = locate_card(tests['input']['cards'], tests['input']['query']) ## This will print the output


# result = locate_card_linear(tests['input']['cards'], tests['input']['query'])
# result = first_and_last_position(tests['input']['cards'], tests['input']['query'])
    ##The function can be tested as follow;

# result = locate_card(**tests['input']) == tests['output'] ## This will test if the result is true or false
# print(result)

# result = locate_card_linear(**tests['input']) == tests['output'] ## This will test if the result is true or false
# print(result)


"""
    Our function should be able to handle any set of valid inputs we pass into it.
    Here's a list of some possible variations we might encounter:

    1. The number query occurs somewhere in the middle of the list cards.

    2. query is the first element in cards.

    3. query is the last element in cards.

    4. The list cards contains just one element, which is query.

    5. The list cards does not contain number query.

    6. The list cards is empty.

    7. The list cards contains repeating numbers.

    8. The number query occurs at more than one position in cards.

    9. (can you think of any more variations?)
    """

# #  The number query occurs somewhere in the middle of the list cards.
# {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output':

# 3}, {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output':

# 6},

# {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},

# {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},

# {'input': {'cards': [6], 'query': 6}, 'output': 0}, {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},

# {'input': {'cards': [], 'query': 7}, 'output': -1}, {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query':

# 3},

# 'output': 7},

# {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6},

# 'output': 2}
# # result = locate_card(tests['input']['cards'], tests['input']['query'])

# locate_card(**tests['input']) == tests['output']


## Question2: Given an array of integers nums sorted in ascending order,
##  find the starting and ending position of a given number.

class Solution:
    def searchRange(self, nums, target):

        # Find the left most target index

        left_target_index = self.binary_search(
            nums,
            target,
            0,
            len(nums) - 1,
            lambda mid_value: mid_value >= target
        )
        
        if left_target_index == -1:
            return [-1, -1]
        
        # Fint the right most target index
        right_target_index = self.binary_search(
            nums,
            target,
            0,
            len(nums) - 1,
            lambda mid_value: mid_value > target
        )
        
        return [left_target_index, right_target_index]
    
    def binary_search(self, nums, target, left, right, predicate):
        best_index_match = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                best_index_match = mid
            
            if predicate(nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
            
        return best_index_match




# Testcase1: when the target occurs more than once 

nums = [5,7,7,8,8,10]
target = 8




# Testcase1: when the target occurs more than once 

# nums = [5,7,7,8,8,8,10]
# target = 8


# Testcase2: When the target is not in the list
# nums = [5,7,7,8,8,10]
# target = 6


# The the target appears once and its in the middle and the array s in decreassing order
# nums = [13, 11, 20, 10, 7, 4, 3, 1, 0]
# target =7


# # The the target appears once and its in the middle and the array s in increasing order
# nums = [0, 1, 3, 4,  7, 10, 11, 13,20]
# target =7


# The list is empty
# nums =[]
# target = 6

# nums = [2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 2, 5, 6, 8]
# target = 2

solution = Solution()
result = solution.searchRange(nums, target)
print(result)



