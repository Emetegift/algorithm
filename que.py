"""
QUESTION:
Several processes are scheduled for execution on an AWS server. On one server, n processes are scheduled where 
the ith process is assigned a priority of priority[i]. the processes are placed sequentially in a queue and are 
numbered 1,2,...n. The server schedules the processes per the following algorithm.

Step 1. If finds the maximum priority shared by at least 2 processes. Let that be denoted by p. If there is no such 
priority or p = 0, the algorithm is terminated

Step 2. Otherwise, select the two of the processes with the lowest indexes and priority p, and call them process1 
and process2.

Step 3. The server executes process1 and removes it from the queue.

Step 4. To avoid starvation, it reduces the priority of process2 to the floor(p/2).

Step 5. Start again from step 1.

Given the initial priority of the processes, find the final priority of the processes which remain after the 
algorithm terminates.

Note that relative to the arrangements of the remaining processes in the queue remains the same, only their 
priorities change.

Example: The number of processes n=6 and their priorities = [6,6,6,1,2,2]
"""

def getPrioritiesAfterExecution(priority):
    while True:
        # Step 1: Find the maximum priority shared by at least 2 processes
        max_priority = max(priority)
        if priority.count(max_priority) < 2 or max_priority == 0:
            break
        
        # Step 2: Select two processes with the lowest indexes and priority p
        process1_index = priority.index(max_priority)
        process1 = max_priority
        priority[process1_index] = 0  # Process 1 is removed
        
        process2_index = priority.index(max_priority)
        process2 = max_priority
        
        # Step 3: Execute process1 and remove it from the queue
        priority[process1_index] = 0
        
        # Step 4: Reduce the priority of process2 to floor(p/2)
        process2_new_priority = max_priority // 2
        priority[process2_index] = process2_new_priority
        
        # Step 5: Continue to the next iteration
    
    # The remaining processes after the algorithm terminates
    remaining_processes = [p for p in priority if p > 0]
    return remaining_processes

# Example input

# Example input
priorities = [6, 6, 6, 1, 2, 2]
# priorities = [6, 6, 1, 3,3, 2]
# priorities = [4, 4, 1, 3, 3, 2]

# Calling the function
final_priorities = getPrioritiesAfterExecution(priorities)
print(final_priorities)



# def maxCopiesAfterUpdates(portalUpdate):
#     inventory = {}  # Dictionary to store book ID counts
#     max_copies = 0  # Maximum copies of any book in the inventory
#     result = []     # List to store results after each update
    
#     for update in portalUpdate:
#         if update > 0:  # Positive update: add a copy to inventory
#             if update not in inventory:
#                 inventory[update] = 0
#             inventory[update] += 1
#             max_copies = max(max_copies, inventory[update])
#         else:  # Negative update: remove a copy from inventory
#             book_id = -update
#             inventory[book_id] -= 1
#             if inventory[book_id] == 0:
#                 del inventory[book_id]
            
#             # Update max_copies if necessary
#             if book_id in inventory:
#                 max_copies = max(max_copies, inventory[book_id])
#             else:
#                 max_copies = 0
        
#         result.append(max_copies)
    
#     return result

# # Sample Input
# # portalUpdate = [1, 2, 4, 1, -1, 2]
# portalUpdate = [1, 2, -1, 2]
# # portalUpdate = [1, 2, 4, 1, -1, 2]

# # Calling the function
# output = maxCopiesAfterUpdates(portalUpdate)

# # Printing the result
# for copies in output:
#     print(copies)



# from collections import deque

# def allocateSeats(n, arr):
#     queue = deque(range(1, n + 1))  # Initialize the queue with seat numbers
#     seat_allocations = {}  # Dictionary to store seat allocations
    
#     for person in arr:
#         while queue:
#             seat = queue[0]
#             if seat == person:
#                 seat_allocations[person] = seat
#                 queue.popleft()  # Allocate the seat and remove the person from the queue
#                 break
#             else:
#                 seat_allocations[queue.popleft()] = seat + 1
#         else:
#             queue.append(person)  # If desired seat is not available, add person to the end of the queue
    
#     return [seat_allocations[person] for person in arr]

# # Example
# n = 5
# arr = [1, 2, 3, 2, 4]
# final_seat_numbers = allocateSeats(n, arr)
# print(final_seat_numbers)  # Output: [1, 2, 3, 5, 4]
