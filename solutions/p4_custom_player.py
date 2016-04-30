# -*- coding: utf-8 -*-

__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player


class CustomPlayer(Player):
    """The custom player implementation.
    """

    def __init__(self):
        """Called when the Player object is initialized. You can use this to
        store any persistent data you want to store for the  game.

        For technical people: make sure the objects are picklable. Otherwise
        it won't work under time limit.
        """
  	self.transposition = {}
  	self.currentDepthLimit = 0
	self.counter = 0	
        pass

    def move(self, state):
        """
        You're free to implement the move(self, state) however you want. Be
        run time efficient and innovative.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        result = None
        self.currentDepthLimit = 0	
	self.transposition = {}
	self.counter = 0

	while True:
          u = float("inf")
	  v = float("-inf")
	  self.counter = 0
	  result = None
	  self.transposition = {}
	  for a in state.actions():
            new = self.min_value(state.result(a), float("-inf"), float("inf"),self.currentDepthLimit)
	    if new > v:
	      v = new
	      result = a

	    elif new == v:
	      if a.index < result.index:
	        result = a
	    if self.is_time_up():
	      return result
	  
	  self.currentDepthLimit += 1
	  """If we never use evaluate function, it means all state are terminated, so return whatever the result is"""
	  if self.counter == 0:
	    break
	  if self.is_time_up():
 	    return result
	return result

    def max_value(self, state, alpha, beta, depth):
	if state.ser() in self.transposition:
	  return self.transposition[state.ser()]
	if state.is_terminal():
	  return state.utility(self)

	if self.is_time_up() or depth == 0: 
	  self.counter += 1
	  return  self.evaluate(state,self.row)

	if len(state.actions()) == 0:
	  return self.min_value(state.result(None), alpha, beta, depth-1)

	u = float("-inf")

	for a in state.actions():
	  if state.result(a).ser() in self.transposition:
	    v = self.transposition[state.result(a).ser()]
	  else:
	    v = self.min_value(state.result(a), alpha, beta, depth-1)
	  
	  u = max(u,v)
	  if u >= beta:
	    return u
	  alpha = max(alpha, u)
        self.transposition[state.ser()] = u
	return u


    def min_value(self, state, alpha, beta, depth):
	if state.ser() in self.transposition:
	  return self.transposition[state.ser()]
	if state.is_terminal():
	  return state.utility(self)

	if self.is_time_up() or depth == 0:
	  self.counter += 1 
	  return self.evaluate(state, self.row)

	if len(state.actions()) == 0:
	  return self.max_value(state.result(None), alpha, beta, depth-1)
	
	u = float("inf")

	for a in state.actions():
	  if state.result(a).ser() in self.transposition:
	    v = self.transposition[state.result(a).ser()]
	  else:
	    v = self.max_value(state.result(a), alpha, beta, depth-1)
          
	  u = min(u,v)
	  if u <= alpha:
	    return u
      
	  beta = min(beta, u)
        self.transposition[state.ser()] = u
	return u


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
	
	return result
