def passToPostFix(redex):
    specials = {'(': 1, "(": 1, '|': 2, '.': 3, '*': 4, '+': 4, '?': 4}
    alfabetoA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'ε']

    resultPostFix = ""
    fixRedex = ""
    redex2 = ""
    redex3 = ""
    stack = []
    stack2 = []
    stack3 = []
    flag = False
    for i, c in enumerate(redex):
        if i+1 != len(redex) and redex[i+1] == '+' and flag == False:
            redex2 += c + '.' + c + '*'
        elif c == '(':
            flag = True
        elif c == ')':
            stack2 = stack2[::-1]
            if '+' in stack2:
                stack22 = stack2.copy()
                redex2 += '('
                while stack2:
                    redex2 += stack2.pop()
                redex2 += ').('
                while stack22:
                    redex2 += stack22.pop()
                redex2 += ')*'
            else:
                while stack2:
                    redex2 += stack2.pop()
            flag = False
        else:
            if flag:
                stack2.append(c)
            elif c != '+':
                redex2 += c

    print("REDEX2", redex2)

    for i, c in enumerate(redex2):
        if i+1 != len(redex2) and redex2[i+1] == '?' and flag == False:
            redex3 += c + '|' + 'ε'
        elif c == '(':
            flag = True
        elif c == ')':
            stack3 = stack3[::-1]
            if '?' in stack3:
                stack32 = stack3.copy()
                redex3 += '('
                while stack3:
                    redex3 += stack3.pop()
                redex3 += ')|('
                while stack32:
                    redex3 += stack32.pop()
                redex3 += ')'
            else:
                while stack3:
                    redex3 += stack3.pop()
            flag = False
        else:
            if flag:
                stack3.append(c)
            elif c != '?':
                redex3 += c

    print("REDEX3", redex3)

    redex = redex3

    for i, c in enumerate(redex):
        if i+1 != len(redex) and c in alfabetoA and redex[i+1] in alfabetoA:
            fixRedex += c + '.'
        elif i+1 != len(redex) and c in alfabetoA and redex[i+1] == '(':
            fixRedex += c + '.'
        elif i+1 != len(redex) and c == ')' and redex[i+1] in alfabetoA:
            fixRedex += c + '.'
        elif i+1 != len(redex) and c == '?' and redex[i+1] in alfabetoA:
            fixRedex += c + '.'
        elif i+1 != len(redex) and c == '*' and redex[i+1] in alfabetoA:
            fixRedex += c + '.'
        elif i+1 != len(redex) and c == '+' and redex[i+1] in alfabetoA:
            fixRedex += c + '.'
        else:
            fixRedex += c

    print('fix redex: a.(a?.b*|c+).b|b.a.a : ', fixRedex)
    for i, c in enumerate(fixRedex):
        if c in alfabetoA:
            resultPostFix += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                resultPostFix += stack.pop()
            stack.pop()
        else:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                resultPostFix += stack.pop()
            stack.append(c)

    while stack:
        resultPostFix += stack.pop()

    return resultPostFix
