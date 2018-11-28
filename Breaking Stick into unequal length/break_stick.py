# -*- coding: utf-8 -*-
"""
    Created on Thu Jul  6 10:40:29 2017
    Artificial Intelligence Assignment
    @author: Muhammad Dawood
    Prgoram Complexity n^k
    Given a stick of length N break this into small stick of different length
"""
import time
import matplotlib.pyplot as plt
import matplotlib.transforms as mtrans


#stick_length_input=1
total_partitions=[]
processing_time=[]
number_partions=[]

def plotResult(X=[],Y=[]):
    """
    This method will plot the result of two array 
    X dimension and Y dimension
    """
    fig = plt.figure(figsize=(12, 14))
    ax = plt.subplot(2, 1, 2)
    trans_offset = mtrans.offset_copy(ax.transData, fig=fig,
                                      x=0.03, y=0.15, units='inches')
    plt.plot(stick_length_input,processing_time,'ro-')
    plt.title('No of Combination VS Input size')
    plt.xlabel('Input size (n)')
    plt.ylabel('No of Combination')
    plt.grid()
    for x, y in zip(X, Y):
        plt.plot((x,), (y,), 'ro')
        plt.text(x, y, '(%d, %d)' % (int(x), int(y)), transform=trans_offset)
    plt.show()
    
    return
    

def cutSub(sub_partition=[],*args):
    
    """
        sub_partition[]:- Show partition which can further be divided into sub partition of higher length
        Deleting last element from the higher partition and append multiple number whose sum is 
        equal to the last element. At the end the modified_partition is added to 
        total_partitions list
    """
    
    first=sub_partition[len(sub_partition)-2]
    last=sub_partition[len(sub_partition)-1]
    modified_partition=sub_partition[:]
    for q in range(first+1,last//2+1):
        if(last-q>q):
            modified_partition=sub_partition[:]
            del modified_partition[len(modified_partition)-1]
            modified_partition.extend([q,last-q])
            total_partitions.append(modified_partition)
    return

def cutRod(stick_length):
    """
        Divide the sub_partition into further partitions
        stick_lenght :- represent length of the stick to be divided into pieces
        total_partitions:- global List of all possible partition
        partition_lenght:- lenght of partion to be splitted into nested sub partion
        piece_index:- show index of the selected sub partition
    """
    
    #recording starting time of program
    start_time=time.clock()
    
    for i in range(1,stick_length//2+1):
        if(stick_length-i>i):
            total_partitions.append([i,stick_length-i])
    partition_length=2
    piece_index=0
    while(partition_length<stick_length//2):
        for piece in range(piece_index,len(total_partitions)):
            if len(total_partitions[piece])==partition_length:
                cutSub(total_partitions[piece][:])
            else:
                piece_index=piece                
                continue
        partition_length=partition_length+1
#    print("Total Number of possible combination ",len(total_partitions))
#    print(time.clock()-start_time," Time consumed in second :: Input size",stick_length_input)
    processing_time.extend([time.clock()-start_time])
    number_partions.extend([len(total_partitions)])
    return
    
    
stick_length_input=[10,20,40,80,100,120,140]
for i in stick_length_input:
    cutRod(i)
plotResult(stick_length_input,number_partions)


