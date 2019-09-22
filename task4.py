def uses_only(word, string):
    for char in word:
        if char not in string:
            return False
    return True

item = open("words.txt")
def uses_only(word, string):
     for char in word:
        if char not in string:
            return False
     return True
     def find_letters():
     uses_only_count = 0
     uses_only_string = raw_input("what are the acceptable letters?")
     for line in item:
        word = line.strip()
        if uses_only(word, uses_only_string):
            print word
            uses_only_count=uses_only_count+1
     print (uses_only_count)

     find_letters()
