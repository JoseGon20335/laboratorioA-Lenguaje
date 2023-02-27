from NFA import *
from createGraph import *

alfabetoA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ε', 'E', 'ϵ']
alfabetoB = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ε', 'E', 'ϵ']
operadores = ['|', '*', '+', '?', '(', ')', '.']
precedence = {'(': 1, "(": 1, '|': 2, '.': 3, '*': 4, '+': 4, '?': 4}


def main():
    # expresion = 'a'
    expresion = 'a|b'
    nfa = NFA().thompson(expresion)
    print(nfa)
    createGraph().createNfa(nfa, alfabetoB)


main()
