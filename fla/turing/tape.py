#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import deepcopy

class Tape:
    def __init__(self, whitespace, tape_alphabet, content=[]):
        self.position = 0 # posicao atual da fita
        self.whitespace_symbol = whitespace
        self.alphabet = tape_alphabet
        self.content = content

    def move_head(self, movement):
        if movement == 'L': 
            self.move_left()
        elif movement == 'R':
            self.move_right()
        elif movement == 'S':
            pass
        else:
            raise ValueError("Invalid direction")

    def move_left(self):
        if self.position > 0: # se existir espaco pra esquerda, vai para a esquerda
            self.position -= 1
        else: # se nao, coloca um branco no comeco da fita (e mantém a posição 0)
            self.content.insert(0,self.whitespace_symbol)

    def move_right(self): 
        if self.position < len(self.content)-1: # se tiver posicao para a direita, vai para a direita
            self.position += 1
        else: # se nao, coloca um espaco em branco na fita e vai para a direita
            whitespace = self.whitespace_symbol
            self.content.append(whitespace)
            self.position += 1

    def get_content(self):
        if len(self.content) == 0:
            return self.whitespace_symbol
        else:
            return self.content[self.position]

    def set_content(self, symbol):
        if len(self.content) == 0:
            self.content.append(symbol)
        else:
            self.content[self.position] = symbol 

    def replace_content(self, new_content):
        self.content = deepcopy(new_content)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        
        return self.content == other.content
        

    def __str__(self):
        result = "(";
        result += str(self.content)
        result += ")@"
        result += str(self.position)
        return result
