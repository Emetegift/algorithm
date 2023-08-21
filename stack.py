
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


   
    
    
    


# # # s = Stack()
# class MinStack:

#     def __init__(self):
#         self.stack = [] #  main stack
#         self.min_stack = []
        

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#         if not self.min_stack or val <= self.min_stack[-1]:
#             self.min_stack.append(val)

#     def pop(self) -> None:
#         if self.stack:
#             if self.stack[-1] == self.min_stack[-1]:
#                 self.min_stack.pop()

#             self.stack.pop()
        

#     def top(self) -> int:
#         if self.stack:
#             return self.stack[-1]
        

#     def getMin(self) -> int:
#         if self.min_stack:
#             return self.min_stack


# # Your MinStack object will be instantiated and called as such:
# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())  # Output: -3
# minStack.pop()
# print(minStack.top())     # Output: 0
# print(minStack.getMin())  # Output: -2

# #To calculate the GPA of a user
# points = {'A+' :5.0, 'A' :4.5, 'A- ':4, 'B+' :3.8, 'B' :3.5, 'B-' :3.0,
#         'C+' :2.8, 'C' :2.5, 'C-' :2, 'D+' :1.5, 'D' :1.0, 'F' :0.0}
# num_courses = 0
# total_point = 0 
# done = False
# while not done:
#     grade = input()
#     if grade == "":
#         done=True

#     elif grade not in points:
#         print("unknown grade '{0}' being ignored".format(grade))
#     else:
#         num_courses += 1
#         total_point += points[grade]
# if num_courses >0:
#     print("Your GPA is {:.3}". format(total_point/num_courses)) 



# def compute_gpa(grades, points={ 'A+': 4.0, 'A': 4.0, 'A-':3.67, 'B+' :3.33,
#                                 'B' :3.0, 'B-' :2.67, 'C+' :2.33, 'C' :2.0,
#                                 'C' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0}):
#     num_courses = 0
#     total_points = 0
#     for g in grades:
#         if g in points: # a recognizable grade
#             num_courses += 1
#             total_points += points[g]
    # return total_points / num_courses
# Code Fragment 1.2: A function that computes a student’s GPA with a point value
# system that can be customized as an optional parameter.

## Example of an Input function in python
# age = int(input( "Enter your age in years:" ))
# max_heart_rate = 206.9 - (0.67 *  age) # as per Med Sci Sports Exerc.
# target = 0.65 * max_heart_rate
# print( "Your target fat-burning heart rate is :",  target)

