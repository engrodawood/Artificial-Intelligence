# -*- coding: utf-8 -*-
"""
    Created on Thu Jul  6 10:40:29 2017
    Artificial Intelligence Assignment
    @author: Muhammad Dawood
    Given a stick of length N break this into small stick of different length
"""
import time

stick_length_input=1
total_partitions=[]
processing_time=[]

def cutSub(stick_length,sub_partition=[],*args):
    
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
            total=0
            for j in modified_partition:
                total+=j**2
            if(total==stick_length**2):
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
    
    for i in range(0,stick_length//2+1):
        if((stick_length-i)**2+i**2==(stick_length)**2):
            if(i==0):
                total_partitions.append([stick_length-i])
            else:
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
    print("Total Number of possible combination ",len(total_partitions))
    print(time.clock()-start_time," Time consumed in second :: Input size",stick_length_input)
    processing_time.extend([time.clock()-start_time])
    return
    
cutRod(99)

