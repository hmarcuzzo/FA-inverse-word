#!/usr/bin/python
# -*- coding: utf-8 -*-

from dfa.transition import Transition

class Instance:
    def __init__(self, automaton, state, word, previous_configuration = None):
        self.automaton = automaton
        self.current_state = state
        self.current_word = word
        self.acceptance_status = None
        self.previous_configuration = previous_configuration

    def __is_transition_valid(self, transition):
        return transition.match(self.current_state, self.current_word[0])

    def __str__(self):
        result = "["
        result += self.current_word
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
        return True

    def is_final(self):
        return len(self.current_word) == 0 or self.acceptance_status != None

    def get_valid_transition(self):
        valid_transitions = []
        for transition in self.automaton.transitions:
            if self.__is_transition_valid(transition):
                valid_transitions.append(transition)
        return valid_transitions[0]
        
    def apply_transition(self, transition):
        if not self.__is_transition_valid(transition):
            return None
        new_instance = Instance(self.automaton, transition.new_state, self.current_word[1:], self)
        return new_instance