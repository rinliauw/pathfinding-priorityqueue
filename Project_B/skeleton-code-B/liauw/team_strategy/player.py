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

        if player == 'upper':
            opponent_player = 'lower'
        else:
            opponent_player = 'upper'
        
        self.player_list = [player, opponent_player] # upper, lower or lower, upper


    def action(self):
        """
        Called at the beginning of each turn. Based on the current state
        of the game, select an action to play this turn.
        """
        # put your code here
    
    def update(self, opponent_action, player_action):
        """
        Called at the end of each turn to inform this player of both
        players' chosen actions. Update your internal representation
        of the game state.
        The parameter opponent_action is the opponent's chosen action,
        and player_action is this instance's latest chosen action.
        """

        action = [opponent_action, player_action]
        for i in range(len(action)):
            if action[i][0] == "THROW": # if throw
                token = Token(action[i][2], action[i][1], self.player_list[i])
                self.board.add_token(token, self.player_list[i])
                # perlu store throw / slide / swing ga?
            else: # if slide or swing, update existing token
                self.board.update_token(action[i], self.player_list[i])
        self.board.turns = self.board.turns + 1


if __name__ == "__main__":
    player = Player('upper')
    player.__init__('upper')
    player.update(("THROW",'s', (-4,2)), ("THROW",'p', (4,-1))) # upper is 4,-1. lower is -4,2
    print(player.board.lower_tokens[0].position) # upper is 4,-1
    print(player.board.upper_tokens[0].position) # lower is -4,2
    player.update(("SLIDE",(-4,2), (-3,1)), ("SLIDE",(4,-1), (3,-1)))
    print(player.board.lower_tokens[0].position) # upper is 4,-1
    print(player.board.upper_tokens[0].position) # lower is -4,2
    print(player.board.turns) # checks if turns is updated