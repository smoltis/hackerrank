def is_matched(expression):
    stack = []
    elements = {'{':'}','[':']','(':')'}

    for item in expression:
        if item in elements.keys():
            stack.append(elements[item])
        elif len(stack) and stack.pop() == item:
            continue
        else:
            return False
    return not stack


if __name__ == "__main__":
    #yes, no, yes
    print(is_matched('{[()]}'))
    print(is_matched('{[(])}'))
    print(is_matched('{{[[(())]]}}'))