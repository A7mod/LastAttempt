from Stack import stack

def match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True 
    else:
        return False          

def balanced(strin):
    s = stack()
    is_balanced = True
    index = 0

    while index < len(strin) and is_balanced:
        paren = strin[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not match(top, paren):
                    is_balanced = False
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False     

print(balanced("(((({}))))"))


