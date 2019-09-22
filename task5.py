def uses_all(word, string):
    for char in string:
        if char not in word:
            return False
    return True
#second half
def uses_all(word, string):
    for char in string:
        if char not in word:
            return False
    return True

item = open("words.txt")

def find_words():
    using_req_letters = 0
    req_letters = raw_input("What are the required letters?")
    req_letters = req_letters.lower()

    for line in item:
        word = line.strip()
        if uses_all(word, req_letters):
            print word
            using_req_letters = using_req_letters+1
    return using_req_letters

find_words()
