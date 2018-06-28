from sys import argv

script, file_name = argv
# Read all
def print_all(f):
    print(f.read())
# Set point
def rewind(f):
    f.seek(0)
# Read line
def print_line(count_line, f):
    print(count_line, f.readline())

current_file = open(file_name)

print("First let's print the whole file: \n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines: \n")

current_line = 1
print(f"Line {current_line}:")
print_line(current_line, current_file)

current_line +=1
print(f"Line {current_line}:")
print_line(current_line, current_file)

current_line +=1
print(f"Line {current_line}:")
print_line(current_line, current_file)
