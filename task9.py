import string
 
punct = [mark for mark in string.punctuation]
spaces = [char for char in string.whitespace]
 
#split into words
def words():
    item= open('origin.txt', 'r')
    main = []
    for line in item:
        for word in line.split():
            main.append(word)
    return main
    data.close()
 
#remove punctuation, whitespace, uppercase
def clear(word1):
    cleared = ''
    for char in word1:
        if (char in punctuations) or (char in whitespaces):
            pass
        else:
            cleared =cleared+char.lower()
    return cleared
         
print ("The book has %s 'words'" % len([clear(word) for word in words()])

