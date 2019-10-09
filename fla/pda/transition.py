#!/usr/bin/python
# -*- coding: utf-8 -*-

class Transition(object):
    def __init__(self, current_state, current_word_symbol, current_stack_symbols, new_state, new_stack_symbols):
        self.current_state =  current_state
        self.current_word_symbol = current_word_symbol
        self.current_stack_symbols = current_stack_symbols
        self.new_state = new_state
        self.new_stack_symbols = new_stack_symbols
                   
    def __str__(self):
        result = "["
        result += self.current_state + ", "
        if not self.has_empty_word_symbol():
            result += self.current_word_symbol
        result += ", "
        if not self.has_empty_current_stack_symbols():
            result += self.current_stack_symbols
        result += " -> "
        result += self.new_state + ", "
        if not self.has_empty_new_stack_symbols():
            result += self.new_stack_symbols
        result += "]"
        return result
    
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if self.current_state != other.current_state:
            return False
        if self.current_word_symbol != other.current_word_symbol:
            return False
        if self.current_stack_symbols != other.current_stack_symbols:
            return False
        if self.new_state != other.new_state:
            return False
        if self.mew_stack_symbols != other.new_stack_symbols:
            return False
        return True
    
    def has_empty_word_symbol(self):
        return self.current_word_symbol == None

    def has_empty_current_stack_symbols(self):
        return self.current_stack_symbols == None

    def has_empty_new_stack_symbols(self):
        return self.new_stack_symbols == None
      
    def match(self, state, word_symbol, stack):
        if self.current_state == state:
            if self.has_empty_word_symbol() or self.current_word_symbol == word_symbol:
                if self.has_empty_current_stack_symbols() or self.current_stack_symbols[::-1] == "".join(stack[-len(self.current_stack_symbols):]):
                    return True
        return False