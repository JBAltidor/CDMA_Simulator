
# test = [1, 2, 3, 34, 6, 7]
# test2 = [2, 3]
# test3 = [3, 5, 6, 7]

# result = []
# def AddVector(a, b):
#     added = []
#     for i in range(min(len(a), len(b))):
#         added.append(a[i]+b[i])
#     if (len(a) > len(b)):
#         added = added + a[i+1:]        
#     elif (len(b) > len(a)):
#         added=added + b[i+1:]       
#     return added


# # result = AddVector(AddVector(test, test2),test3)
# # print (result[:len(test2)])
r=list(range(2**eval(input())))
print([[int(bin(x&y),13)%2 or -1 for x in r]for y in r])