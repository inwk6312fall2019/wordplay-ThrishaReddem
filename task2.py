item = open("words.txt")

def has_no_e(word):
    return "e" not in word


def calculate_no_e():
    total= 0
    no_e_count = 0

    for line in item:
        word = line.strip()
        if has_no_e(word):
            no_e_count =no_e_count+1
            print word
        total=total+1

    no_e= float(no_e_count) / total* 100
    return no_e_percentage
 print calculate_no_e()
