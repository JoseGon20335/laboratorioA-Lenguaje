from graphviz import Digraph
from collections import deque


class createGraph(object):
    """Class representing a state in the NFA."""
    data = None

    def __init__(this, data=None) -> None:
        this.data = data

    def createNfa(this, data):
        # nfa = Digraph('NFA', 'resultado')
        # nfa.graph_attr['rankdir'] = 'LR'  # Left to Right graph orientation

        # transitions = data{'transitions'}
        transitions = data["Transitions"]
        acceptance = data["Acceptance"]
        # Add states and acceptance states to the NFA
        # for state in acceptance:
        #     nfa.node(str(state), shape='doublecircle')
        # nfa.node('start', shape='point')
        for transition in transitions:
            print(transition)
            temp = 0
            for t in transition:
                if temp == 2:
                    print(t)
                temp += 1

                # nfa.node(str(t), shape='circle')

        # Add start and end nodes to the NFA
        # nfa.edge('start', str(transitions[0][0]))

        # return nfa

    def toGraph(self, automaton, name):
        g = Digraph('AFN', filename=name)
        g.attr(rankdir='LR')

        for state in automaton.states.elements:
            if state.type == 'inicial':
                g.node(str(state.id), shape='circle')
                g.node('', shape='none', height='0', width='0')
                g.edge('', str(state.id))

            elif state.type == 'final_inicial':
                g.node(str(state.id), shape='doublecircle')
                g.node('', shape='none', height='0', width='0')
                g.edge('', str(state.id))

            elif state.type == 'final':
                g.node(str(state.id), shape='doublecircle')
            else:
                g.node(str(state.id), shape='circle')

        for transition in automaton.transitions:
            g.edge(str(transition[0].id), str(
                transition[1].id), label=transition[2])

        g.view()
