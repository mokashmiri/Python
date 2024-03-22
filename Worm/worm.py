INPUT_FILE = "seq-long.txt"

def read_line():
    words = list()
    try:
        with open(INPUT_FILE, 'r') as file:
            for line in file:
                words.append(line)
    
    except OSError as problem:
        print(f"Ops,We have problem with : {problem}")
    return(words)

def find_lenght(word1, word2, words):
    word1 = words.find(word1)
    word2 = words.find(word2)
    min_distance = 0
    for word1 in words and word2 in words:
        distance = abs(word1 - word2) - len(word1)
        if distance is None or distance < min_distance:
            min_distance = 0
        
        else:
            print("Ouch,The two words never appear in the same sequence !!")

    else:
        print("these word you chosen does not exist at all !!")

def main():
    print("Insert 2 word, i will tell how close they are !!")
    input("insert first word : ")
    input("insert second word : ")
    
    min_distance = 0
    print(f"Min distance : sequence (distance = {min_distance})")
    

if __name__ == '__main__':
    main()

"""
# Copyright © 2023 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free for personal or classroom use; see 'LICENSE.md' for details.

from pprint import pprint

SEQUENCES_FILE = 'seq.txt'


def find_all(word, sequence):
    indexes = list()
    for i, w in enumerate(sequence):
        if w == word:
            indexes.append(i)
    # ie. indexes = [i for i, w in enumerate(sequence) if w == word]
    return indexes


def read_sequences(filename):
    sequences = list()
    try:
        with open(filename) as input_file:
            for seq in input_file:
                sequences.append(seq.split())
    except OSError as problem:
        print(f"Yeuch: {problem}")
        exit(problem)
    return sequences


def main():
    sequences = read_sequences(SEQUENCES_FILE)
    word1 = input('Enter the first word: ')
    word2 = input('Enter the second word: ')

    min_distance = 0
    sequence_with_min_distance = None
    for i, seq in enumerate(sequences):
        for p0 in find_all(word1, seq):
            # Note: calculating find_all(word2, seq) only once before
            # the for loop would have been somewhat faster
            for p1 in find_all(word2, seq):
                # this code is never executed unless both words are in seq ;-)
                if sequence_with_min_distance is None or abs(p0 - p1) < min_distance:
                    sequence_with_min_distance = i
                    min_distance = abs(p0 - p1)

    if sequence_with_min_distance is not None:
        print(f"Min distance: sequence {sequence_with_min_distance+1} (distance={min_distance})")
    else:
        print("The two words never appear in the same sequence")


if __name__ == '__main__':
    main()
"""