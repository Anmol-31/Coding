def dis(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(dis(1))#actual parameter
print(dis(404))
'''Note the last block: the “variable name” _ acts as a wildcard and never fails to match. If no case
matches, none of the branches is executed.

'''
