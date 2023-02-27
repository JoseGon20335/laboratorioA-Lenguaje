def passToPostFix(redex):
    print("passToPostFix")
    specials = {'*': 5, '+': 4, '?': 3, '.': 2, '|': 1}

    resultPostFix = ""
    stack = []

    for c in redex:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                resultPostFix += stack.pop()
            stack.pop()
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                resultPostFix += stack.pop()
            stack.append(c)
        else:
            resultPostFix += c

    while stack:
        resultPostFix += stack.pop()

    return resultPostFix
