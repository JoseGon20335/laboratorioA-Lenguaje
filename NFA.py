
import postfix


class state:
    label, edge1, edge2 = None, None, None


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
        print("postfix: aa?b*.c+|.b.ba.a.| :", postFix)

        for c in postFix:
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
                accept = state()
                initial = state()

                initial.label = c
                initial.edge1 = accept

                nfaStack.append(NFA(initial, accept))

        this.automata = nfaStack.pop()
        this.prepareResult([this.automata.initial], [])

        return({"Transitions": this.autoTransitions, "Acceptance": this.autoAccept})

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
