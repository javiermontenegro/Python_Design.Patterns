#********************************************************************
# Filename:  StatePattern.py
# Author:    Javier Montenegro (https://javiermontenegro.github.io/)
# Copyright:
# Details:   This code is the implementation of the state pattern.
#*********************************************************************

from abc import ABC, abstractmethod

class State(ABC):
    def handle_state(self):
        pass

class StateA(State):
    def handle_state(self):
        print('State changed to StateA.')

class StateB(State):
    def handle_state(self):
        print('State changed to StateB.')

class Context(State):
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def handle_state(self):
        self.state.handle_state()


if __name__ == "__main__":

    context = Context()
    
    stateA = StateA()
    context.set_state(stateA)
    context.handle_state()

    print('-------------------------------------')

    stateB = StateB()
    context.set_state(stateB)
    context.handle_state()

