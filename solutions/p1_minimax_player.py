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
	amax = (-2, None)
	#self.cache[amax] = float("-inf")
	for a in state.actions():
          """ new is utility"""
	  new = self.min_val(state.result(a))
	  if new > amax[0]:
	    amax = (new, a)
	  elif new == amax[0]:
            if a.index <= amax[1].index:
	      amax = (new,a)
	#amax = self.cache.keys().pop();
	#for k in self.cache.keys():
	#  if self.cache[k] > self.cache[amax]:
	#    amax = k
	#  if self.cache[k] == self.cache[amax]:
	#    if k.index < amax.index:
	#      amax = k
        return amax[1]
	#return max(self.cache, key = lambda k: self.cache[k])

    def max_val(self, state):
	if state.is_terminal():
	  return state.utility(state.player)
	u = float("-inf")
	if len(state.actions()) == 0:
	  return self.min_val(state.result(None))
	for a in state.actions():
	  u = max(u, self.min_val(state.result(a)))
	  #print ("max utility is %d" % u)
	return u

    def min_val(self, state):
	if state.is_terminal():
	  return state.utility(state.player)
	u = float("inf")
	if len (state.actions()) == 0:
          return self.max_val(state.result(None))
	for a in state.actions():
	  u = min(u, self.max_val(state.result(a)))
	  #print ("min utility is %d" % u)
	return u
