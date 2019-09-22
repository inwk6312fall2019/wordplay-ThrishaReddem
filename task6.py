def is_abecedarian(word):
    inital_letter = word[0]
    next_letter = word[1]
    next_index = 1

    while next_index  next_letter:
            return False
        inital_letter = next_letter
        next_index = next_index+1
        next_letter = word[next_index]
    return True

# second half of the question:

item = open("words.txt")

def calculate_abecedarian():
    total_count = 0
    for word in item:
        if is_abecedarian(word):
            print word,
            total_count += 1
    return total_count

calculate_abecedarian()
