# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class MinimaxPlayer(Player):
    def __init__(self):
        self.cache ={}

    def move(self, state):
        """
        Calculates the best move from the given board using the minimax
        algorithm.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        """ utility follows by action"""
	
	v = float("-inf")
	result = None

	for a in state.actions():
          new = self.min_val(state.result(a))
	  if new > v:
 	    v = new
	    result = a
	  elif new == v:
	    if a.index < result.index: 
	      result = a
	return result


    def max_val(self, state):
	if state.is_terminal():
	  return state.utility(self)
	u = float("-inf")
	if len(state.actions()) == 0:
	  return self.min_val(state.result(None))
	for a in state.actions():
	  u = max(u, self.min_val(state.result(a)))
	return u


    def min_val(self, state):
	if state.is_terminal():
	  return state.utility(self)
	u = float("inf")
	if len (state.actions()) == 0:
          return self.max_val(state.result(None))
	for a in state.actions():
	  u = min(u, self.max_val(state.result(a)))
	return u
