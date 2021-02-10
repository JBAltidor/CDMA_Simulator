
test =[1,2,3,34,6,7]
test2=[2,3]
test3 = [3,5,6,7]
su = []
for i in range (max (len(test),len(test2),len (test3))):
    su.append(test[i]+test2[i])

def AddVector(a ,b ):
    added = []
    for i in range (min (len(a),len(b))):
        added.append(a[i]+b[i])
    if (len(a)>len(b)):
        added.append(a[i:])
    elif (len(b)>len(a)):
        


print(su)