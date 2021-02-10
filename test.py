
test = [1, 2, 3, 34, 6, 7]
test2 = [2, 3]
test3 = [3, 5, 6, 7]

result = []
def AddVector(a, b):
    added = []
    for i in range(min(len(a), len(b))):
        added.append(a[i]+b[i])
    if (len(a) > len(b)):
        added = added + a[i+1:]        
    elif (len(b) > len(a)):
        added=added + b[i+1:]       
    return added


print(AddVector(AddVector(test, test2),test3))
