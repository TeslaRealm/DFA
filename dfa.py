from ordered_set import OrderedSet 
import networkx as nx 

'''
A deterministic finite automata (DFA) is a 5-tuple

(S, Σ, δ, s₀, Sₐ)

S ≝ the set of all states in the DFA -> implemented as an ordered set
    Any iterable can be passed as a parameter
    Default value is the empty set
Σ ≝ the alphabet -> implemented as a string of all characters in Σ
    Default value is the empty string
δ(s, c) ≝ the transition function. 
    Given a current state and an input character, δ(s, c) returns the next state.
    Implemented as a dictionary of 2-tuple, generic pairs.
    The 2-tuple represents s, c as described above. The value represents the next state.  
s₀ ≝ the start state
Sₐ ≝ the set of accepting states -> implemented as an ordered set
    Any iterable can be passed as a parameter
'''

class ui(dfa):
    def __init__(self):
        pass

class State():
    def __init__(self, name, value = None, initial = False):
        self.name = name
        self.value = value
        self._initial = initial
        self.identifier = None
        self.transitions = []

class dfa():
    def __init__(self, alphabet, startState, states = OrderedSet(), delta = None, acceptingStates = OrderedSet()):
        self.states = OrderedSet(states)
        self.alphabet = alphabet
        self.delta = delta
        self.acceptingStates = OrderedSet(acceptingStates)

    def addState(self, state):
        states.add(state)

def main():
    states = OrderedSet(['S0', 'S1', 'S2', 'S3'])
    alphabet = 'abc'
    delta = {
        ('S0', 'b') : 'S1',
        ('S1', 'a') : 'S1',
        ('S1', 'b') : 'S2',
        ('S2', 'c') : 'S3',
        ('S3', 'b') : 'S3'
        }
    acceptingStates = OrderedSet(['S3'])
    dfa1 = dfa()

if __name__ == '__main__':
    main()