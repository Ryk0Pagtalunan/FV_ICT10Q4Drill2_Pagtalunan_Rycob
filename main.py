from pyscript import display
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy(e):
    days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
    sold = [4, 3, 5, 7, 2, 1, 6]

    plt.figure()
    plt.plot(days, sold, marker='o', color='yellow')
    plt.title("Milk")
    plt.xlabel("Day")
    plt.ylabel(" Sold")

    display(plt.gcf(), target="output") 


#a = np.array([1,2,3]) #in numpy
#a1 = np.array([4,5,7])
#b = [1,2,3] #regular list
#b1 = [1,2,3]


#print(a + a1)
#print(b)
#print(a * a1)


#a = np.array([[[1,2],[3,4]]])


#print(np.sum(a))
#print(np.mean(a))
#print(np.max(a))
#print(np.m