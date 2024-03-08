import numpy as np
import matplotlib.pyplot as plt

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)

# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}

# plt.title("Sports Watch Data", fontdict = font1, loc = 'left')
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)

# plt.grid(axis = 'y', color = 'red', linestyle = '--', linewidth = 0.5)
# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# plt.scatter(x, y, s=sizes, alpha=0.5)

# plt.show()

y = np.array([35, 25, 25, 15])
mylabels = ["Bollette", "Mutuo", "Spesa", "Divertimento"]

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':12}
plt.title("Spese di famiglia", fontdict = font1, loc = 'left')

plt.pie(y, labels = mylabels)
plt.show() 
