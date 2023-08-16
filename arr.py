# Define a subarray function with array "arr" and list of lists "ans" as parameters
def subarray(arr, ans):

    n = len(arr) # The lengthe of the given array

    # Loop using nested loops for all possible subarrays in the given array
    for start in range(n):# The outer loop (start) select the strating index of the array

        for end in range(start, n): # The inner loop (end) goes from the strating index to the end of the array

            sub = [] # Within the innermost loop a new list called 'sub' is created to store subarrays

            for i in range(start, end + 1): #  loop iterating from the outer index to the inner index thereby populating the the innermost index 'sub'

                sub.append(arr[i]) # the iterated elements are added to sub empty list
            
            ans.append(sub) # The innermost index 'sub' is added to the list of lists 'ans'

# Define a function sum of subarray with subarray list to calculated the sum of subarrays
def sum_of_subarrays(subarray_list):

    total_sum = 0
    for ds in subarray_list:
        unique_elements = set(ds)
        total_sum += len(unique_elements)
    return total_sum

def main():
    arr = [1, 2, 1]
    ans = []

    subarray(arr, ans)
    print(sum_of_subarrays(ans))
    # print(subarray(arr, ans))

if __name__ == "__main__":
    main()



# def subarray(arr, ans):

#     n = len(arr)

#     for start in range(n):
#         for end in range(start, n):
#             sub = []
#             for i in range (start, end + 1):
#                 sub.append(arr[i])
#             ans.append(sub)
