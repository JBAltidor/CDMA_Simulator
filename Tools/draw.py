import matplotlib.pyplot as plt 
  
# x axis values 
x = [121832, 121832, 121832, 487328, 487328, 487328, 524168, 561008, 597848, 634688, 634688, 708352, 782032, 818872, 892560, 892560, 929408, 966240, 957312, 659480]
# corresponding y axis values 
y = [7, 8, 7, 29, 39, 40, 44, 45, 33, 43, 46, 55, 68, 60, 66, 65, 67, 67, 50, 50]
  
# plotting the points  
plt.scatter(x, y, label= "stars", color= "green", marker= ".", s=30) 
# plt.plot(x,y)

  
# naming the x axis 
plt.xlabel('x - Nombre de bits envoyés') 
# naming the y axis 
plt.ylabel('y - Nombre de bits éronnés') 
  
# giving a title to my graph 
plt.title('Noise analysis') 
  
# function to show the plot 
plt.show() 

