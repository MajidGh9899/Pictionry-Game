from concurrent.futures import thread

from  .player import Player
from .board import Board
from .round import Round
class Game(object):
    def __init__(self,id,players):
        self.id = id
        self.players = players
        self.words_used=[]
        self.round=None
        self.board = Board()
        self.player_draw_end=0
        self.connected_thread=thread
        self.start_new_round()
        self.board=Board()

     
    def skip (self):
        
        if self.round:
             new_round=self.round.skip()
             if new_round:
                 self.round_ended()
        else:
            raise Exception("No round stated yet!")
    def start_new_round(self):
        self.round=Round(self.get_word(),self.players[self.player_draw_end],self.players,self)
        
        if self.player_draw_end >= len(self.players) :
            self.end_round()
            self.end_game()
    
    



    def player_guess(self,player,guess):


       return self.round.guess(player,guess)
    def player_disconnected(self,player):
        if self .round:
            self.round.skip()
        else:
            raise Exception("No round started yet")

    def skip(self):
        pass

    def round_ended(self):
        # self.round.skips=0
         self.start_new_round()
         self.board.clear()

    def update_board(self,x,y,color):
        
        if not self.board:
            raise Exception(" No Board created")
        self.board.update(x,y,color)
        
        
        pass
    
    def end_game(self):
        pass 

    def get_word(self):

        pass