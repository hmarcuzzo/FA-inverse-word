#!/usr/bin/python
# -*- coding: utf-8 -*-

class Transition(object):  
    def __init__(self, current_state, current_symbol, new_state):
        self.current_state =  current_state
        self.current_symbol = current_symbol
        self.new_state = new_state
                   
    def __str__(self):
        result = "["
        result += self.current_state + ", " + self.current_symbol + " -> "
        result += self.new_state
        result += "]"
        return result
    
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if self.current_state != other.current_state:
            return False
        if self.current_symbol != other.current_symbol:
            return False
        if self.new_state != other.new_state:
            return False
        return True
    
    def match_state(self, state):
        return self.current_state == state
      
    def match_symbol(self, symbol):
        return self.current_symbol == symbol
      
    def match(self, state, symbol):
        return self.match_state(state) and self.match_symbol(symbol)