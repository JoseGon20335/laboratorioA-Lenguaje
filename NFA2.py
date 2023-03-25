
import postfix


class state:
    label, edge1, edge2 = None, None, None

    def __init__(this, label=None, edge1=None, edge2=None) -> None:
        this.label, this.edge1, this.edge2 = label, edge1, edge2


class Node:
    def __init__(this, name):
        this.name = name
        this.transitions = []


class Transition:
    def __init__(this, symbol, initial, destination):
        this.symbol = symbol
        this.initial = initial
        this.destination = destination


class NFA(object):
    initial, accept = None, None
    automata = None
    data = None

    autoStates = None
    autoSimbols = None
    autoTransitions = None
    autoAccept = None

    def __init__(this, initial=None, accept=None) -> None:
        this.initial, this.accept = initial, accept

    def thompson(this, expresionRegular):
        postFix = postfix.passToPostFix(expresionRegular)
        nfaStack = []
        nfaStack2 = []
        print("postfix: aa?b*.c+|.b.ba.a.| :", postFix)

        for c in postFix:
            nodoNum = 0
            print("c", c)
            if c == '*':
                nfa1 = nfaStack.pop()
                initial = state()
                accept = state()

                initial.edge1 = nfa1.initial
                initial.edge2 = accept
                nfa1.accept.edge1 = nfa1.initial
                nfa1.accept.edge2 = accept

                nfaStack.append(NFA(initial, accept))

            elif c == '.':
                nfa2 = nfaStack.pop()
                nfa1 = nfaStack.pop()

                nfa1.accept.edge1 = nfa2.initial

                nfaStack.append(NFA(nfa1.initial, nfa2.accept))

            elif c == '|':
                nfa2 = nfaStack.pop()
                nfa1 = nfaStack.pop()
                initial = state()

                initial.edge1 = nfa1.initial
                initial.edge2 = nfa2.initial

                accept = state()
                nfa1.accept.edge1 = accept
                nfa2.accept.edge1 = accept

                nfaStack.append(NFA(initial, accept))

            elif c == '+':
                nfa1 = nfaStack.pop()
                accept = state()
                initial = state()

                initial.edge1 = nfa1.initial
                nfa1.accept.edge1 = nfa1.initial
                nfa1.accept.edge2 = accept

                nfaStack.append(NFA(initial, accept))

            elif c == '?':
                nfa1 = nfaStack.pop()
                accept = state()
                initial = state()

                initial.edge1 = nfa1.initial
                initial.edge2 = accept

                nfa1.accept.edge1 = accept
                nfaStack.append(NFA(initial, accept))

            else:

                initial = Node(nodoNum)
                accept = Node(nodoNum + 1)
                transitions = initial.transitions
                transitions.append(Transition(c, initial, accept))
                nfaStack2.append(NFA(initial, accept))

                # ----------------------------------------------
                accept = state()
                initial = state()

                initial.label = c
                initial.edge1 = accept

                nfaStack.append(NFA(initial, accept))

        this.automata = nfaStack.pop()
        this.prepareResult([this.automata.initial], [])
        this.dataToGraph(nfaStack2)
        print("data", this.data)

        return({"Transitions": this.autoTransitions, "Acceptance": this.autoAccept})

    def dataToGraph(this, data):

        print("data", data)

        for i in data:
            nodoTemp = i
            for j in nodoTemp.transitions:
                this.data.append(
                    str('(', i.name, j.symbol, j.destination.name, ')'))

    def prepareResult(this, queue, stack):
        state = queue.pop()

        if state not in stack:
            stack.append(state)

            if state.edge1:
                queue.append(state.edge1)

            if state.edge2:
                queue.append(state.edge2)
        if len(queue) > 0:
            this.prepareResult(queue, stack)
        else:
            stateTemp = this.aceptance(stack, state)
            this.transitions(stack, state, stateTemp)

    def aceptance(this, stack, state):
        allStates = []
        allSimbols = []
        accept = []

        allStatesTemp = {}

        counter = 0
        for state in stack:
            num = str(counter)

            if state == this.automata.accept:
                num = str(len(stack) - 1 + len(accept))
                accept.append(num)
            else:
                allStates.append(num)
                counter += 1

            allStatesTemp[state] = num

            if state.label is None:
                state.label = "E"

            if state.label not in allSimbols:
                allSimbols.append(state.label)

        allStates = allStates + accept

        this.autoStates = allStates,
        this.autoSimbols = allSimbols,
        this.autoAccept = accept
        return(allStatesTemp)

    def transitions(this, stack, state, allStatesTemp):
        allTransitions = []

        for state in stack:
            if state.edge1:
                nextState = (allStatesTemp[state.edge1])

                prev = allStatesTemp[state]
                prevLabel = state.label

                newTransition = "(" + prev + ", " + \
                    prevLabel + ", " + nextState + ")"
                allTransitions.append(newTransition)

            if state.edge2:
                nextState = (allStatesTemp[state.edge2])

                prev = allStatesTemp[state]
                prevLabel = state.label

                newTransition = "(" + prev + ", " + \
                    prevLabel + ", " + nextState + ")"
                allTransitions.append(newTransition)

        this.autoTransitions = allTransitions
