#!/usr/bin/python
# -*- coding: utf-8 -*-

from dfa.dfa import DeterministicFiniteAutomaton
from dfa.transition import Transition as DFATransition 

from ndfa.ndfa import NonDeterministicFiniteAutomaton
from ndfa.transition import Transition as NDFATransition 

from pda.pda import PushDownAutomaton
from pda.transition import Transition as PDATransition 

from turing.turing_machine import TuringMachine
from turing.tape import Tape
from turing.transition import Transition as TuringTransition

import sys
import logging

def dfa(lines, cmdline_args):
    input_alphabet    = lines[0].split()
    states            = lines[2].split()
    initial_state     = lines[3]
    acceptance_states = lines[4].split()
    transitions = []
    for description in lines[5:]:
        splited_description = description.split()
        transition = DFATransition(splited_description[0], splited_description[1], splited_description[2])
        transitions.append(transition)
    dfa = DeterministicFiniteAutomaton(states, initial_state, acceptance_states, transitions)
    initial_configuration = dfa.get_initial_configuration(cmdline_args[0])
    dfa.load_configuration(initial_configuration)
    result = dfa.run()
    if dfa.get_decision() == True:
        print("Aceitou")
    else:
        print("Rejeitou")

def ndfa(lines, cmdline_args):
    input_alphabet    = lines[0].split()
    whitespace        = lines[1]
    states            = lines[2].split()
    initial_states    = lines[3].split()
    acceptance_states = lines[4].split()
    transitions = []
    for description in lines[5:]:
        splited_description = description.split()
        if splited_description[1] == whitespace:
            splited_description[1] = None
        transition = NDFATransition(splited_description[0], splited_description[1], splited_description[2])
        transitions.append(transition)
    ndfa = NonDeterministicFiniteAutomaton(states, initial_states, acceptance_states, transitions)
    initial_configurations = ndfa.get_initial_configurations(cmdline_args[0])
    ndfa.load_configurations(initial_configurations)
    result = ndfa.run()
    if ndfa.get_decision() == True:
        print("Aceitou")
    else:
        print("Rejeitou")

def pda(lines, cmdline_args):
    input_alphabet    = lines[0].split()
    stack_alphabet    = lines[1].split()
    whitespace        = lines[2]
    initial_stack_symbol = lines[3]
    states            = lines[4].split()
    initial_state     = lines[5]
    acceptance_states = lines[6].split()
    transitions = []
    for description in lines[7:]:
        splited_description = description.split()
        if splited_description[1] == whitespace:
            splited_description[1] = None
        if splited_description[2] == whitespace:
            splited_description[2] = None
        if splited_description[4] == whitespace:
            splited_description[4] = None
        transition = PDATransition(splited_description[0], splited_description[1], splited_description[2], splited_description[3], splited_description[4])
        transitions.append(transition)
    pda = PushDownAutomaton(states, initial_state, acceptance_states, initial_stack_symbol, transitions)
    configurations = pda.get_initial_configurations(cmdline_args[0])
    pda.load_configurations(configurations)
    result = pda.run()
    if pda.get_decision() == True:
        print("Aceitou")
    else:
        print("Rejeitou")

def turing_machine(lines, cmdline_args):
    input_alphabet   = lines[0].split()
    tape_alphabet    = lines[1]
    whitespace       = lines[2]
    states           = lines[3].split()
    initial_state    = lines[4]
    final_states     = lines[5].split()
    number_of_tapes  = lines[6]
    transitions = []
    for description in lines[7:]:
        splited_description = description.split()
        transition = TuringTransition(splited_description[0], splited_description[1])
        for tape_part in zip(*(splited_description[2:][i::3] for i in range(3))):
            transition.add_tape_part(tape_part[0], tape_part[1], tape_part[2])
        transitions.append(transition)
    tapes = []
    for i in range(0, int(number_of_tapes)):
        tapes.append(Tape(whitespace, tape_alphabet, list(cmdline_args[i])))
    tm = TuringMachine(states, initial_state, final_states, whitespace, transitions)
    initial_configurations = tm.get_initial_configurations(tapes)
    tm.load_configurations(initial_configurations)
    result = tm.run()
    if result == True:
        if tm.get_decision() == "Accept":
            print("Aceitou")
        else:
            print("Rejeitou")
    else:
        print("Não sei (nunca parou)")


if __name__ == "__main__":
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    fp = open(sys.argv[1], "r") #abre em modo de leitura o arquivo com a definicao da maquina de turing
    lines_cmd = fp.readlines()
    lines = []
    for line in lines_cmd:
        lines.append(line.rstrip())
    automaton_type = lines[0].replace(' ', '')
    lines = lines[1:]
    if automaton_type == "TM":
        turing_machine(lines, sys.argv[2:])
    elif automaton_type == "DFA":
        dfa(lines, sys.argv[2:])
    elif automaton_type == "NDFA":
        ndfa(lines, sys.argv[2:])
    elif automaton_type == "PDA":
        pda(lines, sys.argv[2:])

