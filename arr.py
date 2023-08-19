# # Define a subarray function with array "arr" and list of lists "ans" as parameters
# def subarray(arr, ans):

#     n = len(arr) # The lengthe of the given array

#     # Loop using nested loops for all possible subarrays in the given array
#     for start in range(n):# The outer loop (start) select the strating index of the array

#         for end in range(start, n): # The inner loop (end) goes from the strating index to the end of the array

#             sub = [] # Within the innermost loop a new list called 'sub' is created to store subarrays

#             for i in range(start, end + 1): #  loop iterating from the outer index to the inner index thereby populating the the innermost index 'sub'

#                 sub.append(arr[i]) # the iterated elements are added to sub empty list
            
#             ans.append(sub) # The innermost index 'sub' is added to the list of lists 'ans'

# # Define a function sum of subarray with subarray list to calculated the sum of subarrays
# def sum_of_subarrays(subarray_list):

#     total_sum = 0
#     for ds in subarray_list:
#         unique_elements = set(ds)
#         total_sum += len(unique_elements)
#     return total_sum

# def main():
#     arr = [1, 2, 1]
#     ans = []

#     subarray(arr, ans)
#     print(sum_of_subarrays(ans))
#     # print(subarray(arr, ans))

# if __name__ == "__main__":
#     main()


# """
# QUESTION:
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
# though answers with absolute error of up to  are acceptable.

# Example

# There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

# 0.400000
# 0.400000
# 0.200000
# Function Description

# Complete the plusMinus function in the editor below.

# plusMinus has the following parameter(s):

# int arr[n]: an array of integers
# Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate 
# line with  digits after the decimal. The function should not return a value.

# Input Format

# The first line contains an integer, , the size of the array.
# The second line contains  space-separated integers that describe .

# Constraints



# Output Format

# Print the following  lines, each to  decimals:

# proportion of positive values
# proportion of negative values
# proportion of zeros
# Sample Input

# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
# Sample Output

# 0.500000
# 0.333333
# 0.166667
# """

# #SOLUTION

# # import math
# # import os
# # import random
# # import re
# # import sys

# #
# # Complete the 'plusMinus' function below.
# #
# # The function accepts INTEGER_ARRAY arr as parameter.
# #

# def plusMinus(arr):
#     n = len(arr)
#     j = len([i for i in arr if i > 0])
#     k = len([i for i in arr if i < 0])
#     l = len([i for i in arr if i == 0])

#     print("{:.6f}".format(j/n))
#     print("{:.6f}".format(k/n))
#     print("{:.6f}".format(l/n))

# if __name__ == "__main__":

#     # # Test case 1
#     # arr1 = [1, 2, 0, -1, -2]
#     # plusMinus(arr1)

#     # Test case 2
#     arr2 = [0, 0, 0, 0, 0]
#     plusMinus(arr2)

#     # Test case 3
#     arr3 = [-5, -4, -3, -2, -1]
#     plusMinus(arr3)

#     # Test case 4
#     arr4 = [1, 2, 3, 4, 5]
#     plusMinus(arr4)



"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of 
the five integers. Then print the respective minimum and maximum values as a single line of two space-separated 
long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of  integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

Input Format

A single line of five space-separated integers.

Constraints


Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated 
by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are [1,2,3,4,5] and . Calculate the following sums using four of the five integers:

Sum everything except 1 the sum is 2+3+4+5 .
Sum everything except 2 the sum is 1+3+4+5.
Sum everything except 3 the sum is 2+1+4+5.
Sum everything except 4 the sum is 2+3+1+5.
Sum everything except 5 the sum is 2+3+4+1
 """

 #SOLUTION

def minMaxSum(arr):
   total_sum =sum(arr)

   min_sum = total_sum - max(arr)
   max_sum = total_sum - min(arr)
   print(f"{min_sum}  {max_sum}")

if __name__ == "__main__":
  
   #Testcase1 
   arr1 = [1,2,3,4,5]
   minMaxSum(arr1)

   

   
