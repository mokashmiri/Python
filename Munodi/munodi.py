INPUT_FILE = 'seq.dat'
def munodi(num):
    c = [num]
    while num > 1:
        if num % 2 == 0:
            num = num//2
        else:
            num = 3*num + 1
        c.append(num)
    return c

def read_file(file_name):
    sequence = list()
    try:
        with open(file_name) as file:
            for line in file:
                seq = list()
                for elem in line.strip():
                    if elem.isdigit():
                    
                        seq.append(int(elem))
                sequence.append(seq)
    except OSError as error:
        print(f'file not found: {error}')
    return sequence



def main():
    
    sequence = read_file(INPUT_FILE)
    for num, seq in enumerate(sequence):
        if seq == munodi(seq[0]):
            print(f"sequence {num+1} is a munodi sequence (lenght {len(seq)})")
        else:
            print(f"sequence {num+1} is not a munodi sequence (lenght {len(seq)})")



if __name__ == '__main__':
    main()