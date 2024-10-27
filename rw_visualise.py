import  matplotlib.pyplot as plt

from random_walk import Random_Walk

rw = Random_Walk()
rw.fill_walk()

plt.scatter(rw.x_values,rw.y_values,s=15)
plt.title('Random Walks', fontsize=24)
plt.xlabel('x value', fontsize=14)
plt.ylabel('y value', fontsize=14)
plt.show()
