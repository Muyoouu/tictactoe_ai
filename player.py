from random import choice
import math

# Act as a parent class (blueprint) for all types of player
class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass

# Human player prompts for user input in each turn
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

# Random comp player selects random available box in each turn
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = choice(game.available_moves())
        return square
    
# Smart comp player do min-max algorithm for taking moves in each turn
class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    # Do random moves if having first turn (as the algorithm need at least 1 existing moves to consider)
    # Else, it calls the algorithm function 
    def get_move(self, game):
        if game.count_empty_square() == 9:
            square = choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)["position"]
        return square
    
    def minimax(self, game, letter):
        # Computer is always max player
        max_player = self.letter
        other_player = "O" if letter == "X" else "X"
    
        # Base Case
        # Check if the previous move won
        if game.current_winner == other_player:
            # Score positive if Comp is winner, else negative
            return {"position": None, 
                    "score": 1 * (game.count_empty_square() + 1) if other_player == max_player 
                    else -1 * (game.count_empty_square() + 1)}
        # Return 0 as score if there is no empty squares
        elif not game.empty_square():
            return {"position": None, "score": 0}
        
        # For Comp turn, search for best score as 'max' score
        if letter == max_player:
            best = {"position": None, "score": -math.inf}
        # Otherwise, for Human player search for best score as 'min' score
        else:
            best = {"position": None, "score": math.inf}

        # Simulate each possible move
        for possible_move in game.available_moves():
            game.make_move(possible_move, letter)
            # Recursively call minimax function for each move
            simulation_result = self.minimax(game, other_player)

            # Undo simulation move
            game.board[possible_move] = " "
            game.current_winner = None

            # Set this move in simulation 'position'
            simulation_result["position"] = possible_move

            # For Comp turn, search for best score as 'max' score
            if letter == max_player:
                if simulation_result["score"] > best["score"]:
                    best = simulation_result
            # Otherwise, for Human player search for best score as 'min' score
            else:
                if simulation_result["score"] < best["score"]:
                    best = simulation_result
        return best

