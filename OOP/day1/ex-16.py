# Get something from dict, module, class
"Module style"
def apple():
    print('I have an apple.')

"Dict style"
Mystuff = {
    "apple" : "I AM APLLES"
}
print(Mystuff['apple'])

"Class style"
class Mystuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print("I AM CLASSY APPLES!")

thing  = Mystuff()
thing.apple()
print(thing.tangerine)