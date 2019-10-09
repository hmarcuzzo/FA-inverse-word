#!/usr/bin/python
# -*- coding: utf-8 -*-

from ndfa.instance import Instance
import copy
import logging

class NonDeterministicFiniteAutomaton:
    def __init__(self, states, initial_states, acceptance_states, transitions):
        self.states = states
        self.initial_states = initial_states
        self.acceptance_states = acceptance_states
        self.transitions = transitions
        self.current_configurations = [] 
        self.closure = {}
        for state in self.states:
            self.get_closure(state)   

    def restart(self):
        self.current_configuration = []
        
    def get_closure(self, state):
        if state not in self.closure:
            current_closure = set()
            new_closure = set()
            new_closure.add(state)
            while new_closure != current_closure:
                current_closure.update(new_closure)
                for transition in self.transitions:
                    if transition.match_state(state) and transition.is_empty_transition():
                        new_closure.add(transition.new_state)
            self.closure[state] = new_closure
        return self.closure[state]
    
    def verify_status(self, configuration):
        if len(configuration.current_word) == 0:
            if configuration.current_state in self.acceptance_states:
                configuration.acceptance_status = True
            else:
                configuration.acceptance_status = False
    
    def get_decision(self):
        for configuration in self.current_configurations:
            if len(configuration.current_word) == 0:
                closure = self.get_closure(configuration.current_state)
                if len(closure.intersection(self.acceptance_states)) > 0:
                    return True
        return False

    def get_initial_configurations(self, word):
        configurations = []
        for state in self.initial_states:
            configuration = Instance(self, state, word)
            configurations.append(configuration)
        return configurations
    
    def load_configurations(self, configurations):
        self.current_configurations = configurations

    def step_forward(self):
        configurations_current_step = copy.copy(self.current_configurations)
        self.current_configurations = []
        for configuration in configurations_current_step:
            for transition in configuration.get_valid_transitions():
                new_configuration = configuration.apply_transition(transition)
                if new_configuration is not None:
                    self.current_configurations.append(new_configuration)
                logging.debug(str(configuration) + " -> " + str(new_configuration))

    def run(self):
        pertinence_decision = self.get_decision()
        if pertinence_decision == True:
            return True
        halted_configurations = []
        while self.current_configurations:
            self.step_forward()
            for configuration in self.current_configurations:
                self.verify_status(configuration)
                if configuration.acceptance_status != None:
                    halted_configurations.append(configuration)
        self.current_configurations = halted_configurations
        return self.get_decision()
        
