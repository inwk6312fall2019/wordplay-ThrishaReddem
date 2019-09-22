item = open("words.txt")

def avoid(word, line):
    for char in line:
        if char in word:
            return False
    return True

def avoiding_words():
    avoiding_count = 0
    avoid_string = raw_input("What are the forbidden letters?")
    avoid_string = avoid_string.lower()
#lower coverts all letters into lower case

    for line in fin:
        word = line.strip()
        if avoids(word, avoid_string):
            avoiding_count = avoiding-count+1
    return avoiding_count

print avoid()
