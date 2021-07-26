from Stack import stack

def div(dec):
    s = stack()

    while dec > 0:
        remainder = dec % 2
        s.push(remainder)
        dec = dec // 2

    binary = ""
    while not s.is_empty():
        binary += str(s.pop())
    return binary

print(div(242))


     