import random
import msvcrt
import time
import sys
import os

SIZE = 10
GOLDS = 3
MINER = "X"
DEBUG = True

board = []

def move_player(x, y):
    if DEBUG:
        key = input("Move (W/A/S/D, Q to quit): ").lower()
    else:
        key = msvcrt.getch()
    
    if DEBUG:
        if key == "w": x -= 1
        elif key == "s": x += 1
        elif key == "a": y -= 1
        elif key == "d": y += 1
        elif key == "q": return x, y, "quit"

    else:
        if key == b'\xe0':
            key = msvcrt.getch()
            if key == b'H': x -= 1
            elif key == b'P': x += 1
            elif key == b'K': y -= 1
            elif key == b'M': y += 1
        elif key == b'\x1b':
            return x, y, "quit"

    x = max(0, min(SIZE - 1, x))
    y = max(0, min(SIZE - 1, y))

    return x, y, key

def render(board, x, y):
    
    os.system("cls")  
    
    copy_board = board[:]
    
    for i in range(SIZE):
        for j in range(SIZE):
            if copy_board[i][j] == "🌟":
                copy_board[i][j] = "*"
                
    for i in range(SIZE):
        for j in range(SIZE):
            if i == x and j == y:
                sys.stdout.write(f"{MINER} ") 
            else:
                sys.stdout.write(f"{copy_board[i][j]} ")

        sys.stdout.write("\n")
        
    sys.stdout.flush()

def generate_board():
    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            row.append("*")
    
        board.append(row)
    
    for i in range(GOLDS):
        gen_x = random.randint(0, SIZE - 1)
        gen_y = random.randint(0, SIZE - 1)
        
        board[gen_x][gen_y] = "🌟"
        
def start():
    x, y = 0, 0
    counter = 0    
    status_message = "You found a gold!"
    
    generate_board()
    
    while True:
        x, y, key = move_player(x, y)

        if key == "quit":
            break
        
        if key == "":
            if board[x][y] == "🌟":
                counter += 1
                board[x][y] = "*"
                print(status_message)
                time.sleep(3)
                

            elif board[x][y] == "*":
                status_message = "It's empty! Try again!"
                print(status_message)
                time.sleep(1.5)

        if counter == GOLDS:
            print("You won!")
            break
            
        render(board, x, y)
    
if __name__ == "__main__":
    start()