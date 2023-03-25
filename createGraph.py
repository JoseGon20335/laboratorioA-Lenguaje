from graphviz import Digraph
from collections import deque


class createGraph(object):
    """Class representing a state in the NFA."""
    data = None

    def __init__(this, data=None) -> None:
        this.data = data

    def createNfa(this, data, alfabeto):
        nfa = Digraph('NFA', 'resultado')
        nfa.graph_attr['rankdir'] = 'LR'  # Left to Right graph orientation

        transitions = data["Transitions"]
        acceptance = data["Acceptance"]
        for transition in transitions:
            if transition[0] in acceptance:
                nfa.node(str(transition[0]), shape='doublecircle')
            else:
                nfa.node(str(transition[0]), shape='circle')
            if transition[2] in acceptance:
                nfa.node(str(transition[2]), shape='doublecircle')
            else:
                nfa.node(str(transition[2]), shape='circle')
            nfa.edge(str(transition[0]), str(
                transition[2]), label=transition[1])

        nfa.view()
