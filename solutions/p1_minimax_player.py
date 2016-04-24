# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

import numpy as np
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
	for a in (state.actions()):
	  self.cache[a] = self.min_val(state.result(a))
	return max(self.cache, key = lambda k: self.cache[k])

    def max_val(self, state):
	if state.is_terminal():
	  return state.utility(state.player)
	u = float("-inf")
	for a in state.actions():
	  u = max(u, self.min_val(state.result(a)))
	return u

    def min_val(self, state):
	if state.is_terminal():
	  return state.utility(state.player)
	u = float("inf")
	for a in state.actions():
	  u = min(u, self.max_val(state.result(a)))
	return u
