a = 5
def dis(a):
    a += 5
    print(a)
    return a
dis(dis(dis(dis(5))))    
