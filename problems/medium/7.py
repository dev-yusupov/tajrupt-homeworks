def is_valid(expression):
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map.keys():
            if not stack or brackets_map[char] != stack.pop():
                return False
        else:
            pass
    
    return not stack

expression = "{[()()]}"
print("Is the expression valid?", is_valid(expression))
