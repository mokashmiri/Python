from string import punctuation
File_Name = "strawberry.txt"

def main():
    words = []
    try:
        with open(File_Name) as file:
            for line in file.read().split():
                
                words.append(line.strip(punctuation).upper())

    except OSError as problem:
        print(f"Ooops, we have '{problem}' to open file")

    for i in range(len(words)-2):
        if len(words[i]) == len(words[i+1]) and len(words[i]) == len(words[i+2]):
            print((words[i], words[i+1], words[i+2]))
        
if __name__ == '__main__':
    main()
