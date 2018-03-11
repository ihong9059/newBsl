
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# opens test.text file of the current directory
f = open("test.txt")

# specifying full path
f = open("C:/Python33/README.txt")

# Example 2: Providing mode to open()
# opens for read
f = open("path_to_file", mode='r')

# opens for write
f = open("path_to_file", mode = 'w')

# opens for writing to the end
f = open("path_to_file", mode = 'a')

f = open("path_to_file", mode = 'r', encoding='utf-8')
