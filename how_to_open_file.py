

"""
HOW TO OPEN A FILE AND READ ONLY  using the in-built functionS "open" and ".read()"
"""

fp = open('sample.txt', 'r')  ## This code line will initiate the opening of the sample.txt file in a read mode
# file_content = fp.read()  ## This code reads the entire content and stores it in a file_content vairable

# file_content = fp.read(70) ## This code line will read the first 70 character of the file stored the fp variable

file_content = fp.readline(8) ## Return (remainder of ) the current line of a readable file as a string.

file_content = fp.readlines(9 ) ## Return all (remaining) lines of a readable file as a list of strings.

for line in fp: ## Iterate all (remaining) lines of a readable file.
    pass

file_content = fp.seek(5)  ## Change the current position to be at the kth byte of the file.

'''
fp.tell( ): Return the current position, measured as byte-offset from the start.

fp.write(string): Write given string at current position of the writable file.
fp.writelines(seq): Write each of the strings of the given sequence at the current
position of the writable file. This command does not insert
any newlines, beyond those that are embedded in the strings.
'''



print(file_content) ## This code line will print the file content being accessed

fp.close()  ## Tis will close the file after reading


'''
HOW TO OPEN A FILE AND WRITE ON IT using the in -built functions "open" and "write()"
'''

# fbb = open("sample.text", 'w')

# characters_written = fbb.write("THIS IS A SIMPLE COVER LETTER. \n")

# print(characters_written)
# fbb.close()


'''
HOW TO OPEN A FILE AND APPEND i.e ADD ON IT using the in -built functions "open" and "append()"
'''

# fbb1 = open("sample.text", 'a')

# characters_added = fbb1.write("This was added to the exixting text \n")

# print(characters_added)
# fbb1.close()



