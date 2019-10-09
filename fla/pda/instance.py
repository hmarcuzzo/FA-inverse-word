#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
from pda.transition import Transition

class Instance:
    def __init__(self, automaton, state, word, stack, previous_configuration = None):
        self.automaton = automaton
        self.current_state = state
        self.current_word = word
        self.current_stack = stack
        self.acceptance_status = None
        self.previous_configuration = previous_configuration

    def __is_transition_valid(self, transition):
        if len(self.current_word) == 0:
            current_symbol = None
        else:
            current_symbol = self.current_word[0]
        return transition.match(self.current_state, current_symbol, self.current_stack)

    def __str__(self):
        result = "["
        result += self.current_word + ", "
        result += "".join(self.current_stack)[::-1] + ", "
        result += "]@S"
        result += self.current_state
        return result
    
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if self.current_state != other.current_state:
            return False
        if self.current_word != other.current_word:
            return False
        if self.current_stack != other.current_stack:
            return False
        return True

    def get_valid_transitions(self):
        valid_transitions = []
        for transition in self.automaton.transitions:
            if self.__is_transition_valid(transition):
                valid_transitions.append(transition)
        return valid_transitions
        
    def apply_transition(self, transition):
        if not self.__is_transition_valid(transition):
            return None
        if transition.has_empty_word_symbol():
            new_word = self.current_word
        else:
            new_word = self.current_word[1:]
        new_stack = copy.copy(self.current_stack) 
        if not transition.has_empty_current_stack_symbols():
            for symbol in transition.current_stack_symbols:
                new_stack.pop()
        if not transition.has_empty_new_stack_symbols():
            for symbol in transition.new_stack_symbols[::-1]:
                new_stack.append(symbol)
        new_instance = Instance(self.automaton, transition.new_state, new_word, new_stack, self)
        return new_instance