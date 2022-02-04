import math 
import random 

class Player():
    def __init__(self,letter):
        self.letter=letter

    def get_move(self):
        print("get move function")


class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        got_move=False
        move_val=None
        while not got_move:
            move_val=int(input(f"{self.letter}'s turn, choose move(0-9)"))
            try:
                if move_val not in game.available_moves():
                    raise ValueError
                got_move=True    
            except ValueError:
                print("malfunction: choose a number between 1 to 9, you chose {move_val}")  
        return move_val           

