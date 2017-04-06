# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 16:36:19 2017

@author: Mohammad Imtiaz
"""



import numpy as np
import pandas
import matplotlib.pyplot as plt
from numpy import linalg as la

#desFileNmae - > will reada text file where all the path name of excel files have been saved
desFileNmae = 'D:\\analysis\\fileName.txt'

#content-> content is list of directory which it will hold for reading excel files
with open(desFileNmae) as f:
    content = f.readlines()

#df -> will read the entire excel file
for i in xrange(0, len(content)):
    df = pandas.read_excel(content[i])
    #print df.columns
    
    #then by giving column name each column will be seperated and saved in array
    asmVal = df['ASM'].values
    corrVal = df['Correlation'].values
    dismVal = df['Dissimilarity'].values
    energyVal = df['Energy'].values
    homogenVal = df['Homogenity'].values
    contval = df['contrast'].values
    
    #perfrom mean shift at zero
    asmValMeanSft = asmVal - np.mean(asmVal)
    corrValMeanSft = corrVal - np.mean(corrVal)
    dismValMeanSft = dismVal - np.mean(dismVal)
    energyValMeanSft = energyVal - np.mean(energyVal)
    homogenValMeanSft = homogenVal - np.mean(homogenVal)
    contvalMeanSft = contval - np.mean(contval)
    
  
    #satck all data in matrix transpose wise
    stackVal = np.vstack((asmValMeanSft,corrValMeanSft, dismValMeanSft, energyValMeanSft, homogenValMeanSft, contvalMeanSft))
    
    #calculate coveriance matrix
    covMat = np.cov(stackVal)
    
    #as the input matrix consist of 6 column, we are expecting a 6 by 6 matrix as a covarience result
#    like the follwing matrix
#    C(0,0)	C(0,1)   C(0,2)	C(0,3)   C(0,4)	C(0,5)   
#    C(1,0)	C(1,1)   C(1,2)	C(1,3)   C(1,4)	C(1,5)
#    C(2,0)	C(2,1)   C(2,2)	C(2,3)   C(2,4)	C(2,5)
#    C(3,0)	C(3,1)   C(3,2)	C(3,3)   C(3,4)	C(3,5)
#    C(4,0)	C(4,1)   C(4,2)	C(4,3)   C(4,4)	C(4,5)
#    C(5,0)	C(5,1)   C(5,2)	C(5,3)   C(5,4)	C(5,5)
    
#    where 0 -> ASM, 1 -> correlation, 2 -> dissimilarity, 3 -> energy, 4 -> homogenity, 5 -> contrast 
    
#    So we found from the matrix position value's signed that: 
#    -> ASM and dissimilarity has inversly propotional relationship
#    -> correlation and dissimilarity has inversly propotional relationship
#    -> energy and dissimilarity has inversly propotional relationship
#    -> ASM and contrast has inversly propotional relationship
#    -> correlation and contrast has inversly propotional relationship
#    -> dissimilarity and contrast has propotional relationship
#    -> energy and contrast has inversly propotional relationship
#    -> homogenity and contrast has inversly propotional relationship
#    
#    By checking numbers and sign you can see that the relation between dissimilarity and contrast is highest
    
    print 'covarience matrix of x and y'
    print covMat    
    
    
    #calculate eigen vector and eigen values
    w, v = la.eig(covMat)
    

    print 'eigen values of x and y'
    print w 
    
    print 'eigen vectors of x and y'
    print v
    
    
    
    # curves of all the realtionships are being plotted 
    
    
    plt.figure(1)
    plt.title('Plot of ASM and Dissimilarity data')
    plt.xlabel('data from ASM')
    plt.ylabel('data from Dissimilarity')
    plt.plot(asmValMeanSft, dismValMeanSft, 'ro')
    plt.show(1)  

    plt.figure(2)
    plt.title('Plot of Correlation and Dissimilarity data')
    plt.xlabel('data from Correlation')
    plt.ylabel('data from Dissimilarity')
    plt.plot(corrValMeanSft, dismValMeanSft, 'ro')
    plt.show(2)      
    
    
    plt.figure(3)
    plt.title('Plot of Energy and Dissimilarity data')
    plt.xlabel('data from Energy')
    plt.ylabel('data from Dissimilarity')
    plt.plot(energyValMeanSft, dismValMeanSft, 'ro')
    plt.show(3)  

    plt.figure(4)
    plt.title('Plot of ASM and contrast data')
    plt.xlabel('data from ASM')
    plt.ylabel('data from contrast')
    plt.plot(asmValMeanSft, contvalMeanSft, 'ro')
    plt.show(4)      
    
    plt.figure(5)
    plt.title('Plot of correlation and contrast data')
    plt.xlabel('data from correlation')
    plt.ylabel('data from contrast')
    plt.plot(corrValMeanSft, contvalMeanSft, 'ro')
    plt.show(5)      
    
    
    plt.figure(6)
    plt.title('Plot of dissimilarity and contrast data')
    plt.xlabel('data from dissimilarity')
    plt.ylabel('data from contrast')
    plt.plot(dismValMeanSft, contvalMeanSft, 'ro')
    plt.show(6)     
    
    plt.figure(7)
    plt.title('Plot of Energy and homogenity data')
    plt.xlabel('data from Energy')
    plt.ylabel('data from homogenity')
    plt.plot(energyValMeanSft, homogenValMeanSft, 'ro')
    plt.show(7)     
    
    plt.figure(8)
    plt.title('Plot of Energy and contrast data')
    plt.xlabel('data from Energy')
    plt.ylabel('data from contrast')
    plt.plot(energyValMeanSft, contvalMeanSft, 'ro')
    plt.show(8)  
    
    plt.figure(8)
    plt.title('Plot of homogenity and contrast data')
    plt.xlabel('data from homogenity')
    plt.ylabel('data from contrast')
    plt.plot(homogenValMeanSft, contvalMeanSft, 'ro')
    plt.show(8)    