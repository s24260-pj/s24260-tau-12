from game.board import Board
from game.player import Player

def display_board(board, player_position):
    for i in range(board.rows):
        row = []
        for j in range(board.cols):
            if (i, j) == player_position:
                row.append("P")
            else:
                row.append(board.grid[i][j])
        print(" ".join(row))
    print("\n")

def main():
    board = Board(rows=5, cols=5, obstacle_prob=0.3)
    player = Player(board, start=board.start)

    print("Game Started!")
    display_board(board, player.position)

    while player.position != board.stop:
        move = input("Select player move direction (up, down, left, right) or 'exit': ").strip().lower()
        if move == 'exit':
            print("Game end!")
            break
        if move in ['up', 'down', 'left', 'right']:
            if player.move(move):
                print(f"Move {move} made.")
            else:
                print("Movement impossible (obstacle or end of the board).")
            display_board(board, player.position)
        else:
            print("Incorrect direction of movement. Please try again.")

    if player.position == board.stop:
        print("Congratulations! You have reached the STOP point!")

if __name__ == "__main__":
    main()
