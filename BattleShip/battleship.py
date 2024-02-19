Main_file = "map1.dat"


def read_list(file_name):
    moves = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                move = line.strip().lower()
                moves.append(move)
                
    except OSError as problem:
        print (f"opps : we have a '{problem}")
    return moves

def check_hit(moves, row, col):
    if 0 <= row < len(moves) and 0 <= col < len(moves[0]):
        return moves[row][col] == '#'
    else:
        return False
def play_game(file_name):
    board = read_list(file_name)
    attempts = 0
    hits = 0
    
    while True:
        print("Enter your move (row,col) or type 'quit' to exit:")
        move = input().strip().lower()  # Remove whitespace and convert to lowercase
        if move == 'quit':
            break
        
        try:
            row, col = map(int, move.split(','))  # Split input into row and column
            if check_hit(board, row, col):
                print("Hit!")
                hits += 1
            else:
                print("Miss.")
            attempts += 1
        except ValueError:
            print("Invalid move format. Please enter row,col (e.g., 3,5).")
        except IndexError:
            print("Move out of bounds. Please try again.")

    print(f"Game over. You made {attempts} attempts with {hits} hits.")

if __name__ == "__main__":
    file_name = "map1.dat"  # Ensure this is the correct path to your file
    play_game(file_name)