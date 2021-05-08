from board import Board
from token import Token
class Player:

    def __init__(self, player):
        """
        Called once at the beginning of a game to initialise this player.
        Set up an internal representation of the game state.

        The parameter player is the string "upper" (if the instance will
        play as Upper), or the string "lower" (if the instance will play
        as Lower).
        """
        self.board = Board()


    def action(self):
        """
        Called at the beginning of each turn. Based on the current state
        of the game, select an action to play this turn.
        
        """
        # put your code here
        #self.board.check_finished()
    
    def update(self, opponent_action, player_action):
        """
        Called at the end of each turn to inform this player of both
        players' chosen actions. Update your internal representation
        of the game state.
        The parameter opponent_action is the opponent's chosen action,
        and player_action is this instance's latest chosen action.
        """

        # if (self.board.check_finished()): # checks if game is finished
        #     return

        if opponent_action[0] == "THROW": # if throw
            token = Token(opponent_action[2], opponent_action[1])
            self.board.add_token(token, 'opponent')
            # perlu store throw / slide / swing ga?
        else: # if slide or swing, update existing token
            self.board.update_token([opponent_action[1], opponent_action[2]], 'opponent')
        
        if player_action[0] == "THROW": # if throw
            token = Token(player_action[2], player_action[1])
            self.board.add_token(token, 'mine')
            # perlu store throw / slide / swing ga?
        else: # if slide or swing, update existing token
            self.board.update_token([player_action[1], player_action[2]], 'mine')

if __name__ == "__main__":
    player = Player('upper')
    player.__init__('upper')
    player.update(("THROW",'s', (-4,2)), ("THROW",'p', (4,-1))) # upper is 4,-1. lower is -4,2
    print(player.board.opponent_tokens[0].position) # opponent is -4,2
    print(player.board.my_tokens[0].position) # mine is 4,-1

    player.update(("SLIDE",(-4,2), (-3,1)), ("SLIDE",(4,-1), (3,-1)))
    print(player.board.opponent_tokens[0].position) # opponent is -3,1
    print(player.board.my_tokens[0].position) # mine is 3, -1
    # print(player.board.turns) # checks if turns is updated

    # test if for condition 1
    player.board.throws_count['mine'] = 9
    player.board.defeated_tokens = {'mine': [(0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),(0,8), (0,9)], 'opponent': []}
    player.board.check_finished() # call function
    print("Condition 1 (mine loses):", player.board.status) # mine loses


    player.board.throws_count['opponent'] = 9
    player.board.defeated_tokens = {'mine': [], 'opponent': [(0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),(0,8), (0,9)]}
    player.board.check_finished() # call function
    print("Condition 1 (opponent loses):", player.board.status) # mine loses

    # test for condition 5
    player.board.throws_count['mine'] = 5
    player.board.throws_count['opponent'] = 5
    player.board.defeated_tokens = {'mine': [(0,1), (0,2)], 'opponent': [(0,2), (0,3)]}
    player.board.turns = 360
    player.board.check_finished() # call function
    print("Condition 5 (draw):", player.board.status) # both draw
    player.board.turns = 0

    # test for condition 3
    player.board.throws_count['opponent'] = 9 # max
    player.board.opponent_tokens = [Token((0,1), 'p')]
    player.board.throws_count['mine'] = 5
    player.board.my_tokens = [Token((0,2), 'r'), Token((0,1), 's')]
    player.board.check_finished() 
    print("Condition 3 (mine wins):", player.board.status) # mine win, opponent lose

    # test for condition 3: opponent wins
    player.board.throws_count['mine'] = 9 # max
    player.board.my_tokens = [Token((0,1), 'p')]
    player.board.throws_count['opponent'] = 5
    player.board.opponent_tokens = [Token((0,2), 'r'), Token((0,1), 's')]
    player.board.check_finished() 
    print("Condition 3 (opponent wins):", player.board.status) # mine win, opponent lose

    # test for condition 2: Draw
    player.board.throws_count['mine'] = 9 # max
    player.board.my_tokens = [Token((0,1), 'p'), Token((0,2), 'p')]
    player.board.throws_count['opponent'] = 9
    player.board.opponent_tokens = [Token((0,4), 'r'), Token((0,5), 'p')]
    player.board.check_finished() 
    print("Condition 2 (draw):", player.board.status) # mine win, opponent lose