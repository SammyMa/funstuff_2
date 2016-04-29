# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class AlphaBetaPlayer(Player):

    transposition = set()

    def move(self, state):
        """Calculates the best move from the given board using the minimax
        algorithm with alpha-beta pruning and transposition table.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        u = float("inf")
	v = float("-inf")
	result = None

	self.transposition.add(state.ser())
	for a in state.actions():
	  if state.result(a).ser() in self.transposition:
	    break
	  self.transposition.add(state.result(a).ser())
          new = self.max_value(state.result(a), float("-inf"), float("inf"))
	  if new >= v:
	    v = new
	    result = a
	return result

    def max_value(self, state, alpha, beta):
	if state.is_terminal():
	  return state.utility(self)
	if len(state.actions()) == 0:
	  return self.min_value(state.result(None), alpha, beta)
	u = float("-inf")
	for a in state.actions():
	  if state.result(a).ser() in self.transposition:
	    break
	  u = max(u, self.min_value(state.result(a), alpha, beta))
	  self.transposition.add(state.result(a).ser())
	  
	  if u >= beta:
	    return u
	  alpha = max(alpha, u)
	return u

    def min_value(self, state, alpha, beta):
	if state.is_terminal():
	  return state.utility(self)
	if len(state.actions()) == 0:
	  return self.max_value(state.result(None), alpha, beta)
	u = float("inf")
	for a in state.actions():
	  if state.result(a).ser() in self.transposition:
	    break
	  self.transposition.add(state.result(a).ser())
	  u = min(u, self.max_value(state.result(a), alpha, beta))
	  if u <= alpha:
	    return u
	  beta = min(beta, u)
	return u
