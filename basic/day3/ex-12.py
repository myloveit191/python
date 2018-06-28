#Name, Variable, Code and Functions

# This on is like your scripts with argv
def print_two(*argv):
    arg1, arg2 = argv
    print(f"arg1: {arg1}, arg2: {arg2}")

# Ok, that *argv is actually poinless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one argument

def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no argument
def print_none():
    print("I got nothin'.")

print_two("Nghia","LopD14PM01")
print_two_again("Khoa Ky Thuat Cong Nghe", "DH Thu Dau Mot")
print_one("Sinh vien nam cuoi")
print_none()
