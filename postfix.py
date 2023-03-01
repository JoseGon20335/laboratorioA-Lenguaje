def passToPostFix(redex):
    specials = {'*': 5, '+': 4, '?': 3, '.': 2, '|': 1}
    alfabetoA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    resultPostFix = ""
    fixRedex = ""
    stack = []

    for i, c in enumerate(redex):
        if i+1 != len(redex) and c in alfabetoA and redex[i+1] in alfabetoA:
            fixRedex += c + '.'
        elif i+1 != len(redex) and c in alfabetoA and redex[i+1] == '(':
            fixRedex += c + '.'
        elif i+1 != len(redex) and c == ')' and redex[i+1] in alfabetoA:
            fixRedex += c + '.'
        else:
            fixRedex += c

    print(fixRedex)
    for i, c in enumerate(fixRedex):
        print(c)
        if c in alfabetoA:
            if i+1 != len(fixRedex) and c in alfabetoA and fixRedex[i+1] in alfabetoA:
                resultPostFix += c + '.'
            else:
                resultPostFix += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                resultPostFix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and specials.get(c, 0) <= specials.get(stack[-1], 0):
                resultPostFix += stack.pop()
            stack.append(c)

    while stack:
        resultPostFix += stack.pop()

    return resultPostFix
