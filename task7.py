def has_double(word):
    for i in range(len(word) - 5):
            if word[i] == word[i + 1]:
                if word[i + 2] == word[i + 3]:
                    if word[i + 4] == word[i + 5]:
                        return True
    return False

item= open("words.txt")

def find_doubles():
    for line in item:
        word = line.strip()
        if has_double(word):
            print word

find_doubles()

