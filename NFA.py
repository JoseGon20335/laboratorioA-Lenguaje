
import postfix


class Node:
    def __init__(this, name):
        this.name = name
        this.transitions = []


class Transition:
    def __init__(this, symbol, destination):
        this.symbol = symbol
        this.destination = destination


class NFA(object):
    autoTransitions = []
    autoAccept = []
    valorSuma = ''

    def __init__(this, nodes=None) -> None:
        this.nodes = nodes

    def thompson(this, expresionRegular):
        postFix = postfix.passToPostFix(expresionRegular)
        nfaStack = []
        print("postfix: aa?b*.c+|.b.ba.a.| :", postFix)
        nodoNum = 0
        for c in postFix:
            print("c", c)
            if c == '*':
                print("entro *", c)
                candado = nfaStack.pop()
                candado1 = candado.nodes[0]  # 0
                candado2 = candado.nodes[1]  # 1
                nodo1 = Node(nodoNum)  # 2
                nodoNum += 1
                nodo2 = Node(nodoNum)  # 3

                simbolo = ''
                transitions = candado1.transitions
                for transition in transitions:
                    if transition.destination == candado2:
                        simbolo = transition.symbol
                        transition.symbol = 'ε'

                transitions = candado2.transitions
                transitions.append(Transition(simbolo, nodo1))

                transitions = nodo1.transitions
                transitions.append(Transition('ε', candado2))
                transitions.append(Transition('ε', nodo2))

                transitions = nodo2.transitions
                transitions.append(Transition('ε', candado1))

                # grupo = [candado1, candado2]
                # nfaStack.append(NFA(grupo))
                # grupo = [nodo1, nodo2]
                # nfaStack.append(NFA(grupo))
                grupo = [candado1, candado2, nodo1, nodo2]
                nfaStack.append(NFA(grupo))
                this.autoAccept.pop()
                this.autoAccept.append(nodo2.name)

            elif c == '.':
                nodoG2 = nfaStack.pop()
                nodoG1 = nfaStack.pop()
                nodo1 = nodoG1.nodes.pop()
                nodo2 = nodoG2.nodes[0]
                # tomo el segundo elemento del nodo2

                nodo1.transitions.append(Transition('.', nodo2))
                # transitions = nodo1.transitions
                # transition.append(Transition('.', nodo2))
                nodoG1.nodes.append(nodo1)
                nfaStack.append(nodoG1)
                nfaStack.append(nodoG2)

            elif c == '|':
                orExp2 = nfaStack.pop()
                orExp1 = nfaStack.pop()
                orExp11 = orExp1.nodes[0]  # 0 a
                orExp12 = orExp1.nodes[1]  # 1
                orExp21 = orExp2.nodes[0]  # 2 b
                orExp22 = orExp2.nodes[1]  # 3
                nodo1 = Node(nodoNum)  # 4
                nodoNum += 1
                nodo2 = Node(nodoNum)  # 5

                simbolo = ''
                transitions = orExp11.transitions
                for transition in transitions:
                    if transition.destination == orExp12:
                        simbolo = transition.symbol
                        transition.symbol = 'ε'

                transitions = orExp12.transitions
                transitions.append(Transition(simbolo, orExp21))

                simbolo = ''
                transitions = orExp21.transitions
                for transition in transitions:
                    if transition.destination == orExp22:
                        simbolo = transition.symbol
                        transitions.remove(transition)

                transitions = orExp11.transitions
                transitions.append(Transition('ε', orExp22))

                transitions = orExp22.transitions
                transitions.append(Transition(simbolo, nodo1))

                transitions = nodo1.transitions
                transitions.append(Transition('ε', nodo2))

                transitions = orExp21.transitions
                transitions.append(Transition('ε', nodo2))

                # grupo = [orExp11, orExp12]
                # nfaStack.append(NFA(grupo))
                # grupo = [orExp21, orExp22]
                # nfaStack.append(NFA(grupo))
                # grupo = [nodo1, nodo2]
                # nfaStack.append(NFA(grupo))
                grupo = [orExp11, orExp12, orExp21, orExp22, nodo1, nodo2]
                nfaStack.append(NFA(grupo))
                this.autoAccept.pop()
                this.autoAccept.append(nodo2.name)

            else:
                nodo1 = Node(nodoNum)
                nodoNum += 1
                nodo2 = Node(nodoNum)
                transitions = nodo1.transitions
                transitions.append(Transition(c, nodo2))
                this.valorSuma = c
                grupo = [nodo1, nodo2]
                nfaStack.append(NFA(grupo))
                if this.autoAccept != []:
                    this.autoAccept.pop()
                    this.autoAccept.append(nodo2.name)
                else:
                    this.autoAccept.append(nodo2.name)

            nodoNum += 1

        this.dataToGraph(nfaStack)
        print("data", this.autoTransitions)

        return({"Transitions": this.autoTransitions, "Acceptance": this.autoAccept})

    def dataToGraph(this, data):

        for i in data:
            nodes = i.nodes
            for j in nodes:
                for y in j.transitions:
                    res = j.name, y.symbol, y.destination.name
                    this.autoTransitions.append(res)
