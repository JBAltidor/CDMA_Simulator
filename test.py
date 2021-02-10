
test =[1,2,3,34,6,7]
test2=[2,3]
test3 = [3,5,6,7]
su = []
for i in range (min (len(test),len(test2))):
    su.append(test[i]+test2[i])


print(su)