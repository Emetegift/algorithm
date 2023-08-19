
# """
# Data structure tutorial exercise: Stack
# QUESTION 1:
# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# """

# from collections import deque

# class Stack:
#     def __init__(self):
#         self.container = deque()
   

#     def push(self, val): ## Used to add values to a stack list
#         self.container.append(val)

#     def pop(self): ## Used to remove values from stack
#         return self.container.pop()
    
#     # def peek(self): ## Used to return the value in the stack without deleting it
#     #     return self.container[-1]
    
#     # def is_empty(self):
#     #     return len(self.container)==0
    
#     def size(self): ## Used to get the length of stack list
#         return len(self.container)
 
#     # def __str__(self):
#     #     return str(self.container)

# def reverse_string(s): ## This function is used to reverse the position of values
#     stack = Stack()

#     for char in s:
#         stack.push(char)

#     rstr = ''
#     while stack.size()!=0:
#         rstr += stack.pop()
#     return rstr


# if __name__ == '__main__':
#     print(reverse_string("We will conquere COVID-19"))

#     print(reverse_string("I am the king"))

#     print(reverse_string("GIFT"))
#     # print(reverse_string(13567))


   
    
    
    


# # s = Stack()
class MinStack:

    def __init__(self):
        self.stack = [] #  main stack
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()

            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2







