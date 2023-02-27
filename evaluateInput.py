class evaluaInput(object):

    def __init__(this, inputData=None, alfabeto=None, operadores=None, precedence=None) -> None:
        this.inputData = inputData
        this.alfabeto = alfabeto
        this.operadores = operadores
        this.precedence = precedence

    def evalute(this, input):
        result = input
        if(input == ''):
            return 'No se ingreso un redex'
        if(input == ' '):
            return 'No se ingreso un redex'

        result = input.replace(' ', '').replace(
            'ε', 'E').replace('ϵ', 'E').replace('/', '|')

        for c in input:
            if(c not in this.alfabeto and c not in this.operadores):
                return 'El redex contiene el siguiente componente no valido: ' + c

        parentesis = this.evaluarParentesis(result)

        if(parentesis == False):
            return 'Error en los parentesis, algun parentesis no tiene pareja. :( porfa no lo dejes solito'

        parentesis = this.evaluarParentesis2(result)

        if(parentesis == False):
            return 'Error en los parentesis, uno de ellos esta vacio. Un parentesis vacio no tiene obetvios en la vida, tristesa.'

        return result

    def evaluarParentesis(input):
        stack = []
        for c in input:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0:
                    return False
                stack.pop()
        return len(stack) == 0

    def evaluarParentesis2(input):
        stack = []
        for c in input:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0:
                    return False
                if stack[-1] == '(':
                    return False
                stack.pop()
            else:
                if len(stack) > 0 and stack[-1] == '(':
                    stack.append(None)
        return True

    def evaluarOperadorBinario(input):
        stack = []
        for i, c in enumerate(input):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack) == 0:
                    return False
                stack.pop()
            else:
                if c in "+-*|" and (len(stack) == 0 or stack[-1] == '(') and (i == 0 or s[i-1] == '(' or s[i-1] in "+-*|"):
                    return False
        return len(stack) == 0
