

edit

play_arrow

brightness_4
import matplotlib.pyplot as plt 
  
# x axis values 
x = [1,2,3,4,5,6] 
# corresponding y axis values 
y = [2,4,1,5,2,6] 
  
# plotting the points  
plt.plot(x, y, color='green',  linewidth = 3, 
         marker='x', markerfacecolor='blue', markersize=6) #linestyle='dashed',
  
# setting x and y axis range 
plt.ylim(1,8) 
plt.xlim(1,8) 
  
# naming the x axis 
plt.xlabel('x - Nombre de bits envoyés') 
# naming the y axis 
plt.ylabel('y - Nombre de bits éronnés') 
  
# giving a title to my graph 
plt.title('Noise analysis') 
  
# function to show the plot 
plt.show() 

