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
	amin = (-2, None)
	#self.cache[amax] = float("-inf")
        """check for which player we are dealing with"""
	
	for a in state.actions():
          new = self.max_val(state.result(a))
	  if new >= amin[0]:
 	    amin = (new, a)
	  """elif new == amin[0]:
	    if a.index < amin[1].index:
	      amin = (new, a)"""
	return amin[1]
	#amax = self.cache.keys().pop();
	#for k in self.cache.keys():
	#  if self.cache[k] > self.cache[amax]:
	#    amax = k
	#  if self.cache[k] == self.cache[amax]:
	#    if k.index < amax.index:
	#      amax = k
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
