def more_than_20(file):
    words = []
    data = open(file, 'r')
    words = [x.strip() for x in data if len(x.strip()) > 20]
    return words

print(more_than_20("CROSSWD.txt"))


def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True


word = 'allegory'
print(has_no_e(word))


def uses_only(word, letters):
    for x in word:
        if x not in letters:
            return False
    return True
    
def all_uses_only(file, letters):
    data = open(file, 'r')
    words = []
    for x in file:
        words = [x.strip() for x in letters if uses_only(x.strip(), letters) == True]
    return words


print(all_uses_only("CROSSWD.txt", 'abrz'))








