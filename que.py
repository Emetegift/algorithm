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
# priorities = [6, 6, 6, 1, 2, 2]
# priorities = [6, 6, 1, 3,3, 2]
priorities = [4, 4, 1, 3, 3, 2]

# Calling the function
final_priorities = getPrioritiesAfterExecution(priorities)
print(final_priorities)
