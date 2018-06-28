# Cho mot chuoi thuc hien cac hanh dong sau:
#   - Tach chuoi thanh mang
#   - Sap xep chuoi sau khi tach
#   - Lay phan tu dau tien hoac cuoi cung cua mang

# Doi ten ex-15 thanh ex15
def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """This is function sorts words."""
    return sorted(words)

def print_first_word(words):    
    """Prints the first word after popping it off."""        
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Print the last word after poping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence ):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

# import ex1
# Goi ham: ex15.tenham(thamso)