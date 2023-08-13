# Question on Product of Array Except Self
'''
To solve this problem, we can use the concept 
of prefix and suffix products. 
We'll first calculate the prefix products, 
which are the products of all elements to the 
left of each element. Then, we'll calculate the 
suffix products, which are the products of all 
elements to the right of each element. Finally,
 we'll multiply the prefix and suffix products 
at each index to get the desired output array.
'''

# def productExceptSelf(nums):
#     n = len(nums)

#     #Initialize the output array with 1

#     output =[1] * n

#     # Calculate the prefix product

#     prefix_product = 1
#     for i in range(n):
#         output[i] *= prefix_product
#         prefix_product *= nums[i]

#     # Calculate the suffix product
#     suffix_product = 1
#     for i in range(n -1,-1,-1):
#         output[i] *= suffix_product
#         suffix_product *= nums[i]

#     return output

# # nums=[1,2,3,4]
# # output = productExceptSelf(nums)
# # print(output)

# nums=[-1,1,0,-3,3]
# output = productExceptSelf(nums)
# print(output)


def productExceptSelf(nums):

    n =len(nums)

    # initialize the output with 1
    output =[1] * n

    #Calculate the prefix product
    prefix_product = 1
    
    for i in range(n):
        output[i] *= prefix_product
        prefix_product *= nums[i]

    # Calculate suffix_product
    suffix_product = 1

    for i in range(n -1,-1,-1):
        output[i] *= suffix_product
        suffix_product *= nums[i]
    return output

nums = [1,2,3,4,5,4]
output = productExceptSelf(nums)
print(output)

        



# # Question2: Maximum Product Subarray

# def maxProductSubarray(nums):
#     n = len(nums)
#     if n == 0:
#         return 0

#     # Initialize variables to track the maximum product
#     max_product = nums[0]
#     curr_max = nums[0]
#     curr_min = nums[0]

#     for i in range(1, n):
#         # Calculate the new maximum product by considering both positive and negative numbers
#         if nums[i] < 0:
#             curr_max, curr_min = curr_min, curr_max

#         # Update the current maximum and minimum subarray products
#         curr_max = max(nums[i], curr_max * nums[i])
#         curr_min = min(nums[i], curr_min * nums[i])

#         # Update the maximum product if a larger value is found
#         max_product = max(max_product, curr_max)

#     return max_product

# nums = [2, 3, -2, 4]
# output = maxProductSubarray(nums)
# print(output)