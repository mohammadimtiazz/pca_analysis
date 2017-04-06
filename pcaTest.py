# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 16:23:56 2017

@author: Mohammad Imtiaz
"""

import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt



def extended(ax, x, y, **args):

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    x_ext = np.linspace(xlim[0], xlim[1], 100)
    p = np.polyfit(x, y , deg=1)
    y_ext = np.poly1d(p)(x_ext)
    ax.plot(x_ext, y_ext, **args)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    return ax




#two different data set
x = [2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1]
y = [2.4,0.7,2.9,2.2,3.0,2.7,1.6,1.1,1.6,0.9]

print 'dataset x'
print x

print 'dataset y'
print y

#normalize both dataset so that both of their mean is adjusted at 0
meanX = np.mean(x)
meanY = np.mean(y)

x1 = x - meanX;
y1 = y - meanY;


print 'mean adjusted dataset x'
print x1

print 'mean adjusted dataset y'
print y1


# plot of original x and y data
plt.figure(1)
plt.title('Plot of x an y data')
plt.xlabel('data from X')
plt.ylabel('data from Y')
plt.plot(x, y, 'ro')
plt.show(1)


#plot of mean adjusted data of x and y
plt.figure(2)
plt.title('Plot of mean shifted at 0 of x an y data')
plt.xlabel('data from X1')
plt.ylabel('data from Y1')
plt.plot(x1, y1, 'bo')
plt.show(2)


#stack both of the data Set like this
#if stack doesn't look like this use matrix transpose to do that
xyConCat = np.vstack((x1,y1))

print 'stack of both data set x and y'
print xyConCat


xyCov = np.cov(xyConCat)

print 'covarience matrix of x and y'
print xyCov

#xyCov(0,0) -> present varience of data x
#xyCov(1,1) -> present varience of data y
#varience also represents spreading of data. higher value means more spreading and vice versa

#xyCov(0,1) and xyCov(1,0) boths sign are important 
#+ sign represent both dimension increase tother
# - sign represnt if one dimension increase other decrease
# zero represents two dimensions are independent of each other




#Eigen values and vectors of covarience matrix
# w -> presents eigen values 
# v -> presents eigen vectors
w, v = la.eig(xyCov)


#As expected from the covariance matrix,they two variables do indeed increase together.
#See how one of the eigenvectors goes through the middle of the points, like drawing a line of best fit? That
#eigenvector is showing us how these two data sets are related along that line. The second eigenvector gives us the other, 
#less important, pattern in the data, that all the points follow the main line, but are off to the side of the main line by some amount.


#the eigenvalues are quite different. In fact, it turns out that
#the eigenvector with the highest eigenvalue is the principle component of the data set.
#In our example, the eigenvector with the larges eigenvalue was the one that pointed
#down the middle of the data. It is the most significant relationship between the data
#dimensions.

print 'eigen values of x and y'
print w 

print 'eigen vectors of x and y'
print v


plt.figure(3)
plt.title('Plot of mean shifted at 0 of x an y data with both eigen vector')
plt.xlabel('data from X1')
plt.ylabel('data from Y1')
plt.plot(x1, y1, 'bo')
plt.plot(v[0,0], v[1,0], 'r+')
plt.plot(v[0,1], v[1,1], 'r+')
plt.show(3)


# this part used for extending lines from both eigen vectors 
vx1 = np.linspace(v[0,0], 0.0, 25)
vy1 = np.linspace(v[1,0], 0.0, 25)

vx2 = np.linspace(v[0,1], 0.0, 25)
vy2 = np.linspace(v[1,1], 0.0, 25)

plt.figure(4)
plt.title('Plot of mean shifted at 0 of x an y data with both eigen vector')
plt.xlabel('data from X1')
plt.ylabel('data from Y1')
plt.plot(x1, y1, 'bo')
plt.plot(v[0,0], v[1,0], 'r+')
plt.plot(v[0,1], v[1,1], 'r+')
plt.plot(vx1, vy1, 'g-')
plt.plot(vx2, vy2, 'g-')
plt.grid(4)
ax = plt.subplot(111)
ax = extended(ax, vx1, vy1,  color="g", lw=1)
ax = extended(ax, vx2, vy2,  color="r", lw=1)
#ax.plot(vx2, vy2, color="g", lw=4, label="short")
plt.show(4)
