"""

# Big O notation
A linear regression is formed when the time at
 which a program runs is directly proportional
#  to the size of the program i.e 0(n)

"""
# ## To find the square of a number
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers
numbers = [2,5,8,9]
print(get_squared_numbers(numbers))
# print(numbers)



# # A function whose order of complexity is 1, i.e 0(1)

# def find_first_pe(prices, eps, index):
#     pe = prices[index]/eps[index] # The supply of index does a constant operation irrespective of the price

#     return pe

# ##when looking for the duplicate of a list, i.e 0(n2)
def duplicate(numbers):
   
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]==numbers[j]:
                print (numbers[i], "is a duplicate")
                break

numbers = [3, 6, 2, 4, 6, 8, 9]
print(duplicate(numbers))



#Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function



max = int(input("Enter max number: "))

even_numbers = []

for i in range(1, max):
    if i % 2 == 0:
        even_numbers.append(i)

print("Even numbers: ", even_numbers)


max = int(input("Enter max number "))
odd_number = []

for i in range(1, max):
    if i % 2 ==1:
        odd_number.append(i)
print("Odd Number is:", odd_number)
