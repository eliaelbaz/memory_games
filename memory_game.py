import random

def init_game() -> dict:
    """
    Initialize the game data including board, score, turn, and move history.
    Returns a dictionary containing all game data.
    """
    # Create a shuffled deck with pairs of cards
    deck = list('AABBCCDDEEFF')
    random.shuffle(deck)

    game_data = {
        'rows': 4,
        'columns': 3,
        'board': deck,
        'score': {'player1': 0, 'player2': 0},
        'turn': 'player1',
        'game_over': False,
        'move_history': []
    }

    return game_data

def display_board(game_data):
    """
    Display the current state of the board.
    """
    board = game_data['board']
    board_state = ['_' if i not in game_data['move_history'] else board[i] for i in range(len(board))]
    for i in range(0, len(board_state), game_data['columns']):
        print(' '.join(board_state[i:i + game_data['columns']]))

def make_move(game_data, index1, index2):
    """
    Handle the player's move, checking for matches and updating the game state.
    """
    board = game_data['board']
    if board[index1] == board[index2]:
        print(f"Match found: {board[index1]} and {board[index2]}")
        game_data['move_history'].extend([index1, index2])
        game_data['score'][game_data['turn']] += 1
    else:
        print(f"No match: {board[index1]} and {board[index2]}")

def switch_turn(game_data):
    """
    Switch the turn between players.
    """
    game_data['turn'] = 'player2' if game_data['turn'] == 'player1' else 'player1'

def check_game_over(game_data):
    """
    Check if the game is over.
    """
    if len(game_data['move_history']) == len(game_data['board']):
        game_data['game_over'] = True
        print("Game over! All pairs have been found.")
        return True
    return False

def play(game_data):
    """
    Main function to manage the game loop.
    """
    while not game_data['game_over']:
        display_board(game_data)
        print(f"{game_data['turn']}'s turn.")

        try:
            index1 = int(input("Enter the index of the first card to flip (0-11): "))
            index2 = int(input("Enter the index of the second card to flip (0-11): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 11.")
            continue

        if index1 == index2 or index1 not in range(12) or index2 not in range(12):
            print("Invalid indices. Please choose two different indices within the range 0-11.")
            continue

        make_move(game_data, index1, index2)
        if not check_game_over(game_data):
            switch_turn(game_data)
