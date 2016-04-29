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
        self.maxDepth = 0   
  	self.currentDepthLimit = 0
	
        pass

    def move(self, state):
        """
        You're free to implement the move(self, state) however you want. Be
        run time efficient and innovative.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """
        result = None
	maxDepthLimit = state.M*state.N+1

	while self.is_time_up() == False and self.currentDepthLimit <= maxDepthLimit:
          """Clear the transposition table"""
	  self.currentDepthLimit += 1

          u = float("inf")
	  v = float("-inf")
	  result = None
		
	  self.transposition[state.ser()] = result
	  for a in state.actions():
	    if state.result(a).ser() in self.transposition:
	      new = self.transposition[state.result(a).ser()]
	    else:
              new = self.max_value(state.result(a), float("-inf"), float("inf"), 1)
	      self.transposition[state.result(a).ser()] = new 
	    if new >= v:
	      v = new
	      result = a
	    """return the result is time is up, disregarding of whether this is the best move or not"""
 	    if self.is_time_up() == True:
	      return result
	return result

    def max_value(self, state, alpha, beta, depth):
	if state.is_terminal():
	  return state.utility(self)

	if self.is_time_up() or depth > self.currentDepthLimit:
	  return self.evaluate(state, state.player_row)

	if len(state.actions()) == 0:
	  return self.min_value(state.result(None), alpha, beta, depth)

	u = float("-inf")

	for a in state.actions():
	  if state.result(a).ser() in self.transposition:
	    u = self.transposition[state.result(a).ser()]
	  else:
	    u = max(u, self.min_value(state.result(a), alpha, beta, depth+1))
	    self.transposition[state.result(a).ser()] = u
	  
	  if u >= beta:
	    return u

	  alpha = max(alpha, u)

	return u


    def min_value(self, state, alpha, beta, depth):
	if state.is_terminal():
	  return state.utility(self)

	if self.is_time_up() or depth > self.currentDepthLimit:
	  return self.evaluate(state, state.player_row)

	if len(state.actions()) == 0:
	  return self.max_value(state.result(None), alpha, beta, depth)
	
	u = float("inf")

	for a in state.actions():
	  if state.result(a).ser() in self.transposition:
	    u = self.transposition[state.result(a).ser()]
	  else:
	    u = min(u, self.max_value(state.result(a), alpha, beta, depth+1))
            self.transposition[state.result(a).ser()] = u
	  if u <= alpha:
	    return u

	  beta = min(beta, u)

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
	#print("result is %f" % result)
	return result
