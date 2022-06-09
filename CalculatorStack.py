def compute_last_op(stack):
    equation = [stack.pop(),stack.pop(),stack.pop()]

    if equation[1] == "-":
        stack.append(int(equation[2]) - int(equation[0]))
    elif equation[1] == "+":
        stack.append(int(equation[0]) + int(equation[2]))
    elif equation[1] == "*":
        stack.append(int(equation[0]) * int(equation[2]))
    elif equation[1] == "/":
        stack.append(int(equation[2]) // int(equation[0]))

def evaluate(s):
    s = s.replace(" ", "")
    stack = []
    first_digit = False
    start_index = 0
    for index in range(len(s)):
        if s[index].isdigit():

            if not first_digit:
                first_digit = True
                start_index = index
            if index == len(s) - 1:
                num = s[start_index:index+1]
                stack.append(num)
                print(index,': ', s[index])


        else:
            # must be an operator here!
            if first_digit:
                # let's capture the number
                num = s[start_index:index]
                # push into stack
                first_digit = False
                start_index = 0
                stack.append(num)
            # encounter some operator here
            if s[index] in '*/':
                if len(stack) > 1 and stack[-2] in "*/":
                    compute_last_op(stack)
                stack.append(s[index])

            elif s[index] in '+-':
                if len(stack) > 1:
                    compute_last_op(stack)
                stack.append(s[index])
    while len(stack) > 1:
        compute_last_op(stack)
    return stack


print(evaluate("40/8+2*5"))
