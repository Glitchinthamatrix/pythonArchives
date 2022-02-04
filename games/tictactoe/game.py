import random
import math
from player import HumanPlayer,RandomComputerPlayer

class TicTacToe():
    def __init__(self):
        self.board=[' ' for i in range(9)]
        self.current_winner=None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)] :
            print("|"+"|"+row+"|")  

    @staticmethod
    def print_board_nums():
        number_board=[[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]  
        for row in number_board:
            print("|"+"|".join(row)+"|")  
    
    def winner(self,square,letter):
        row_ind=math.floor(square/3)
        row=self.board[row_ind:(row_ind+1)*3]
        if all([s==letter for s in row]):
            return True

        col_ind=square%3
        col=[self.board[col_ind+(i*3)] for i in range(3)] 
        if all([s==letter for s in col]):
            return True

        if square%2==0:
            diagonal1=[self.board[i] for i in [0,4,8]]
            diagonal2=[self.board[i] for i in [2,4,6]]

            if all([s==letter for s in diagonal1]):
                return True    

            if all([s==letter for s in diagonal2]):
                return True  
        return False          


    def available_moves(self):      
        # moves=[]  
        # for i,spot in enumerate(self.board):
        #     if spot==" ":
        #         moves.append(i)
        # return moves        

        #or do the same thing like this (the effiicient way)   
        return [i for i,spot in enumerate(self.board) if i==" "] 

    def has_empty_squares(self):
        return False if len(self.available_moves())<1 else True

    def empty_square_num(self):
        return len(self.available_moves)  

    def make_move(self,square,letter):
        if self.board[square]==" ":
            self.board[square]=letter   
            if self.winner(square,letter):
                self.current_winner=letter
            return True   
        return False    

def play(game, x_player,o_player,print_game=True):
    if print_game:
        game.print_board_nums()

    letter='x'
    while game.has_empty_squares():
        if letter=='X':
            square=x_player.get_move()
        else:
            square=o_player.get_move()

        if game.make_move(square,letter):
            if print_game:
                print(f"{letter} made move to square {square}") 
                game.print_board()           
                print("")

            if game.current_winner():
                print(f"{letter} wins!")
                return letter    
            letter = 'X' if letter =='O' else 'X'

    if print_game:
        print("It's a tie")        

if __name__=="__main__":
    game=TicTacToe()
    o_player=RandomComputerPlayer('O')
    x_player=HumanPlayer('X')
    play(game,x_player,o_player,print_game=True)
