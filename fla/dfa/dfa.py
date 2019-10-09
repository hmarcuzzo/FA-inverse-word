#!/usr/bin/python
# -*- coding: utf-8 -*-

from dfa.instance import Instance
import logging

class DeterministicFiniteAutomaton:
    def __init__(self, states, initial_state, acceptance_states, transitions):
        self.states = states
        self.initial_state = initial_state
        self.acceptance_states = acceptance_states
        self.transitions = transitions
        self.current_configuration = None    

    def restart(self):
        self.current_configuration = None
            
    def get_decision(self):
        if len(self.current_configuration.current_word) == 0:
            if self.current_configuration.current_state in self.acceptance_states:
                return True
            else:
                return False
        return None

    def get_initial_configuration(self, word):
        return Instance(self, self.initial_state, word)
    
    def load_configuration(self, configuration):
        self.current_configuration = configuration

    def step_forward(self):
        transition = self.current_configuration.get_valid_transition()
        if transition == None:
            if len(self.current_configuration.current_word) == 0 and self.current_configuration.current_state in self.acceptance_states:
                self.current_configuration.acceptance_status = True
            else:
                self.current_configuration.acceptance_status = False
        else:
            self.current_configuration = self.current_configuration.apply_transition(transition)

    def run(self):
        logging.debug(self.current_configuration)
        pertinence_decision = self.get_decision()
        if pertinence_decision == True:
            return True
        while not self.current_configuration.is_final():
            self.step_forward()
            logging.debug(self.current_configuration)
        return self.get_decision()
        