# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class AlphaBetaPlayer(Player):

#transposition = {}

    def move(self, state):
        """Calculates the best move from the given board using the minimax
        algorithm with alpha-beta pruning and transposition table.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        u = float("inf")
	v = float("-inf")
	result = None
	self.transposition = {}
	for a in state.actions():
	  new = self.min_value(state.result(a), float("-inf"), float("inf"))
	  if new > v:
	    v = new
	    result = a
	  elif new == v:
	    if a.index < result.index:
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
	    v = self.transposition[state.result(a).ser()]
	  else:
	    v = self.min_value(state.result(a), alpha, beta)
	  u = max(u,v)   
#  self.transposition[state.ser()] = u
	  
	  if u >= beta:
	    return u
	  alpha = max(alpha, u)
	
        self.transposition[state.ser()] = u
	return u


    def min_value(self, state, alpha, beta):
#	if state.ser in self.
	if state.is_terminal():
	  return state.utility(self)
	if len(state.actions()) == 0:
	  return self.max_value(state.result(None), alpha, beta)
	u = float("inf")
	for a in state.actions():
	  if state.result(a).ser() in self.transposition:
	    v = self.transposition[state.result(a).ser()]
	  else:
	    v = self.max_value(state.result(a), alpha, beta)
	  u = min(u,v)  
	  
	  if u <= alpha:
	    return u
	  beta = min(beta, u)
	
	self.transposition[state.ser()] = u
	return u
