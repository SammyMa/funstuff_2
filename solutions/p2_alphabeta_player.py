# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class AlphaBetaPlayer(Player):

    def move(self, state):
        """Calculates the best move from the given board using the minimax
        algorithm with alpha-beta pruning and transposition table.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
	u = self.max_value(state, float("-inf"), float("inf"))
	for a in state.actions():
	  new = self.min_value(state.result(a), float("-inf"), float("inf"))
	  if new == u:
	    return a
	return None

    def max_value(self, state, alpha, beta):
	if state.is_terminal():
	  return state.utility(state.player)
	if len(state.actions()) == 0:
	  return self.min_value(state.result(None), alpha, beta)
	u = float("-inf")
	for a in state.actions():
	  u = max(u, self.min_value(state.result(a), alpha, beta))
	  if u >= beta:
	    return u
	  alpha = max(alpha, u)
	return u

    def min_value(self, state, alpha, beta):
	if state.is_terminal():
	  return state.utility(state.player)
	if len(state.actions()) == 0:
	  return self.max_value(state.result(None), alpha, beta)
	u = float("inf")
	for a in state.actions():
	  u = min(u, self.max_value(state.result(a), alpha, beta))
	  if u <= alpha:
	    return u
	  beta = min(beta, u)
	return u
