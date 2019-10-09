#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

from turing.transition import Transition

class Instance:
    def __init__(self, automaton, state, tapes = [], previous_configuration = None):
        self.automaton = automaton
        self.current_state = state
        self.tapes = copy.deepcopy(tapes)
        self.previous_configuration = previous_configuration
        self.acceptance_status = None

    def is_transition_valid(self, transition):
        current_tape_symbols = []
        for tape in self.tapes:
            current_tape_symbols.append(tape.get_content())
        return transition.match(self.current_state, current_tape_symbols)
        
    def get_valid_transitions(self):
        valid_transitions = []
        for transition in self.automaton.transitions:
            if self.is_transition_valid(transition):
                valid_transitions.append(transition)
        return valid_transitions

    def apply_transition(self, transition):
        if self.acceptance_status != None:
            return self
        if not self.is_transition_valid(transition):
            return None
        new_instance = Instance(self.automaton, transition.get_new_state(), self.tapes, self)
        for tape in zip(new_instance.tapes, transition.get_new_tape_data()):
            tape[0].set_content(tape[1][0])
            tape[0].move_head(tape[1][1])
        return new_instance

    def __str__(self):
        result = "["
        for tape in self.tapes:
            result += str(tape)
            result += ","
        result += "]@S"
        result += self.current_state
        return result
    
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        
        if self.current_state != other.current_state:
            return False
        
        if self.tapes != other.tapes:
            return False
