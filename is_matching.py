def is_matching(expression):
    expression = list(expression)
    parenthesis1 = 0
    parenthesis2 = 0
    for index in expression:
        if index == "(":
            parenthesis1 += 1
        elif index == ")":
            parenthesis1 -= 1
        elif index == "[":
            parenthesis2 += 1
        elif index == "]":
            parenthesis2 -= 1
    if parenthesis1 == 0 and parenthesis2 == 0:
        return True
    else:
        return False
