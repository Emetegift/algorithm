# # How to carryout Linkedlist process

# class Node: ## This represents an individual element in the linkedlist
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
#             itr = itr.next
#         print(llstr)

#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next

#         return count

#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return

#         itr = self.head

#         while itr.next:
#             itr = itr.next

#         itr.next = Node(data, None)

#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.insert_at_begining(data)
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break

#             itr = itr.next
#             count += 1

#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.head = self.head.next
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break

#             itr = itr.next
#             count+=1

#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)


#     def insert_after_value(self, data_after, data_to_insert):
#     # Search for first occurance of data_after value in linked list
#     # Now insert data_to_insert after data_after node

#         current = self.head
#         while current is not None:
#             if current.data == data_after:
#                 break
#             current = current.next

#         # If data_after value is not found in the linked list
#         if current is None:
#             print(f"{data_after} not found in the linked list.")
#             return

#         # Create a new node with data_to_insert
#         new_node = Node(data_to_insert)

#         # Insert the new node after the node with data_after value
#         new_node.next = current.next
#         current.next = new_node


#     # def remove_by_value(self, data):
#     # Remove first node that contains data


# if __name__ == '__main__':
#     # ll = LinkedList()
#     # ll.insert_values(["banana","mango","grapes","orange"])
#     # ll.insert_at(1,"blueberry")
#     # ll.remove_at(2)
#     # ll.print()

#     # ll.insert_values([45,7,12,567,99])
#     # ll.insert_at_end(67)
#     # ll.print()


#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print()
#     ll.insert_after_value("mango","apple") # insert apple after mango
#     ll.print()
#     # ll.remove_by_value("orange") # remove orange from linked list
#     # ll.print()
#     # ll.remove_by_value("figs")
#     ll.print()
#     # ll.remove_by_value("banana")
#     # ll.remove_by_value("mango")
#     # ll.remove_by_value("apple")
#     # ll.remove_by_value("grapes")
#     ll.print()



"""
Question on Linkedlist:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""
# Solution


# # Define a class to represent a node in a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# # Define a class for the solution
class Solution:
    # This function takes two linked lists l1 and l2 as input and returns the sum as a linked list.
    def addTwoNumbers(self, l1, l2):
        # Initialize a variable to keep track of any carry or overflow while adding digits.
        # This concept is often referred to as "carry" because you're carrying a value
        # from one place to another, just like when you add numbers manually.
        carry = 0
        
        # Create a result linked list to store the sum of digits.
        res = n = ListNode(0)
        
        # Loop until both linked lists are exhausted and there's no more carry left.
        while l1 or l2 or carry:
            # Add the values of corresponding nodes from l1 and l2 along with any carry from the previous step.
            if l1:
                carry += l1.val
                l1 = l1.next
                
            if l2:
                carry += l2.val
                l2 = l2.next
                
            # Calculate new carry and digit value for the result node.
            carry, val = divmod(carry, 10)
            
            # Create a new node with the calculated digit value and connect it to the result linked list.
            n.next = n = ListNode(val)
            
        # Return the next node after the initial 0 as the actual result linked list.
        return res.next

# Create linked list nodes for l1 and l2
l1 = ListNode(2, ListNode(4, ListNode(3)))  # Represents the number 342
l2 = ListNode(5, ListNode(6, ListNode(4)))  # Represents the number 465

# Create an instance of the Solution class
solution = Solution()

# Call the addTwoNumbers function to add the two linked lists and get the result
output = solution.addTwoNumbers(l1, l2)  # Result represents the number 807

# Print the values of the linked list nodes in the output
while output:
    print(output.val, end=" ")  # Print each digit of the sum
    output = output.next  # Move to the next node

# Output: 7 0 8 (represents the sum 807)
