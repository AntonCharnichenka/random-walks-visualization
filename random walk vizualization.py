"""This module contains a logic that allows to build random walks visualizations"""

# import
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# create and visualize random walk data set
while True:
    random_walk = RandomWalk(50000)  # random walk data set will consist of 50000 points
    random_walk.fill_walk()

    points_numbers = list(range(random_walk.num_points))

    # set plot size
    plt.figure(figsize=(10, 6))  # in inches
    # set plot title
    plt.title('Random walk visualization: {} points'.format(len(points_numbers)), loc='center')
    # plot random walk
    plt.scatter(random_walk.x_values, random_walk.y_values, c=points_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    # highlight first and last points in the random walk
    plt.scatter(0, 0, c='green', edgecolor='none', s=50, label='start point')
    plt.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c='red', edgecolor='none', s=50, label='end point')
    plt.legend(loc='upper left')
    # remove axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input('Create another walk? (y/n): ')
    if keep_running == 'n':
        break
