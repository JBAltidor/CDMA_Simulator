import matplotlib.pyplot as plt 
  
# x axis values 
x = [4288, 9000, 11168, 33528, 44720, 55904, 67080, 78256, 89432, 100608, 111784, 122960, 134152]
# corresponding y axis values 
y = [0, 0, 0, 2, 2, 1, 4, 0, 0, 5, 0, 0, 1128] 
  
# plotting the points  
plt.scatter(x, y, label= "stars", color= "green", marker= ".", s=30) 


  
# naming the x axis 
plt.xlabel('x - Nombre de bits envoyés') 
# naming the y axis 
plt.ylabel('y - Nombre de bits éronnés') 
  
# giving a title to my graph 
plt.title('Noise analysis') 
  
# function to show the plot 
plt.show() 

