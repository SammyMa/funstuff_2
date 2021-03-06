# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action


class EvaluationPlayer(Player):
    def move(self, state):
        """Calculates the best move after 1-step look-ahead with a simple
        evaluation function.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """

        # *You do not need to modify this method.*
        best_value = -1.0

        actions = state.actions()
        if not actions:
            actions = [None]

        best_move = actions[0]
        for action in actions:
            result_state = state.result(action)
            value = self.evaluate(result_state, state.player_row)
            if value > best_value:
                best_value = value
                best_move = action

        # Return the move with the highest evaluation value
        return best_move

    def evaluate(self, state, my_row):
        """
        Evaluates the state for the player with the given row
        """
	stoneonmyside = 0.00
	stoneonopside = 0.00
	result = 0.00
	for a in range(0,state.M+1):
	  stoneonmyside += state.board[a]
        
	for a in range(state.M+1, 2*(state.M)+1):
	  stoneonopside += state.board[a]

	if my_row == 0:
	  result = (stoneonmyside - stoneonopside) / (2*(state.M)*(state.N))
	else:
	  result = (stoneonopside - stoneonmyside) / (2*(state.M)*(state.N))
	#print("result is %f" % result)
	return result
	

