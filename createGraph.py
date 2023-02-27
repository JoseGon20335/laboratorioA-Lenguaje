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
            nfa.node(str(transition[1]), shape='circle')
            if transition[7] in acceptance:
                nfa.node(str(transition[7]), shape='doublecircle')
            else:
                nfa.node(str(transition[7]), shape='circle')
            nfa.edge(str(transition[1]), str(
                transition[7]), label=transition[4])

        nfa.view()
