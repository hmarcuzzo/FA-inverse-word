#!/usr/bin/python
# -*- coding: utf-8 -*-

from turing.instance import Instance

import copy
import logging

class TuringMachine:
    def __init__(self, states, initial_state, final_states, whitespace, transitions):
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.whitespace = whitespace
        self.current_configurations = []

    def get_initial_configurations(self, tapes):
        return [Instance(self, self.initial_state, tapes)]
    
    def load_configurations(self, configurations):
        self.current_configurations = configurations

    def restart(self, tapes):
        self.current_configurations = []

    def verify_status(self, configuration):
        if configuration.acceptance_status != None:
            configuration.acceptance_status
        for final_state in self.final_states:
            if configuration.current_state == final_state:
                configuration.acceptance_status = True
                return True
        valid_transitions = configuration.get_valid_transitions()
        if len(valid_transitions) == 0:
            configuration.acceptance_status = False
            return False

    def is_halted(self):
        if len(self.current_configurations) == 0:
            return True
        for configuration in self.current_configurations:
            if configuration.acceptance_status != None:
                return True 
        return False

    def get_decision(self):
        for configuration in self.current_configurations:
            if configuration.acceptance_status == True:
                return "Accept"
        if len(self.current_configurations) == 0 or self.is_halted():
            return "Reject"
        return "Undefined"
        
    def step_forward(self):
        configurations_current_step = copy.copy(self.current_configurations)
        self.current_configurations = []
        for configuration in configurations_current_step:
            logging.debug(str(configuration))
            for transition in configuration.get_valid_transitions():
                new_configuration = configuration.apply_transition(transition)
                self.current_configurations.append(new_configuration)
                logging.debug(str(configuration) + " -> " + str(new_configuration))
            
    def run(self):
        halted_configurations = []
        for configuration in self.current_configurations:
            self.verify_status(configuration)
            if configuration.acceptance_status != None:
                halted_configurations.append(configuration)
            logging.debug(str(configuration) + " (" + str(configuration.acceptance_status) + ")")
        while self.current_configurations:
            self.step_forward()
            for configuration in self.current_configurations:
                self.verify_status(configuration)
                if configuration.acceptance_status != None:
                    halted_configurations.append(configuration)
                logging.debug(str(configuration) + " (" + str(configuration.acceptance_status) + ")")
        self.current_configurations = halted_configurations
        if self.is_halted():
            return True
        
