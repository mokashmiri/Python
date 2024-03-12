It_Name = "parole_italiane.txt"


def read_list(file_name):
    words = list()
    try:
        with open(file_name) as fin:
            words = fin.read().split('\n')
    except OSError as problem:
        print(f"Yeuch: {problem}")
    return words

def misspell(word1, word2):
    if len(word1) != len(word2):
        return False
    num_diff = 0
    for w1, w2 in zip(word1.upper(), word2.upper()):
        if w1 != w2:
            num_diff += 1
    return num_diff == 1

def main():
    names = read_list(input('insert the file and the name you want :\n'))
    words = read_list(It_Name)

    for n in names:
        misspelled = False
        print(f"\n Name: {n}:")
        for w in words:
            if misspelled == True:
                print(f"{w}")
        if not misspelled:
            print("warning: no misspelled words found")

def misspell_alt(word1,word2):
    set1 = set(enumerate(word1.upper()))
    set2 = set(enumerate(word2.upper()))
    return len(word1) == len(word2) and len(set1.symmetric_difference(set2)) == 2

if __name__ == '__main__':
    main()