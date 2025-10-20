#print(type(words_file))
#for line in words_file:
    #print(line)
#This keeps it from itrating forever. 
#It will never stop without a defined stopping point

#words = []
#print(type(words_file))
#for line in words_file:
#    print(line)
    #words.append(line.strip())


# print(words)
#strip gets rid of white space before and after


# print([x for x in dir(words_file) if '_' != x[0] ])

# print(words_file.readline())
# print(words_file.readline())

# data = [1, 3, 2, 8, 5 , 6, 10]
# print([2*x for x in data if x % 2 == 0])



# can x be used like a normal variable in commands?

# (route to file, interaction with file)
# r = read
# w = overwrites data in file
# a = appending data to file

#file = open('CROSSWD.txt', 'r')

#def twenty_or_more(file):
#    file = open(file, 'r')
#    Ch20 = []
#    if [x for x in dir(file) if ]
#        for line in file:
#            print(line.strip())


def more_than_20(file):
    words = []
    data = open(file, 'r')

#    for word in data:
#        if len(word.strip()) > 20:
#            words.append(word.strip())

    words = [x.strip() for x in data if len(x.strip()) > 20]
    return words

print(more_than_20("CROSSWD.txt"))

def has_no_e(word):
    word = ''
    if 'e' in word.strip(): 
        return True
    else:
        return False


word = 'allegory'
print(has_no_e(word))



#def uses_only(word, letters)
    
#def all_uses_only(file, letters)








