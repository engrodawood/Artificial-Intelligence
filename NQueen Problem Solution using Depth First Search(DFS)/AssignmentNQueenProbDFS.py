# -*- coding: utf-8 -*-
"""
    Created on Thu Jul  16 10:40:29 2017
    Artificial Intelligence Assignment
    @author: Muhammad Dawood
    N-Queen Problem
    Given a chessBoard of N*N Calcualte the N Queen not attacking each other.
"""

import time
import matplotlib.pyplot as plt
import matplotlib.transforms as mtrans


  #***********************************************************************************
    #********************************* Method For ploting Result *******************
    #**********************************************************************************
def plotResult(X=[],Y=[]):
    """
    This method will plot the result of two array 
    X dimension and Y dimension
    """
    fig = plt.figure(figsize=(12, 14))
    ax = plt.subplot(2, 1, 2)
    trans_offset = mtrans.offset_copy(ax.transData, fig=fig,
                                      x=0.03, y=0.15, units='inches')
    plt.plot(X,Y,'ro-')
    plt.title('Time VS Input size')
    plt.xlabel('Input size (n)')
    plt.yscale('log')
    plt.ylabel('Time (t)')
    plt.grid()
    for x, y in zip(X, Y):
        plt.plot((x,), (y,), 'ro')
        plt.text(x, y, '(%d, %0.5f)' % (int(x), float(y)), transform=trans_offset)
    plt.show()

    return

class NQueenSolution:

    boardSize=0
    queenBoard=[]
    number_queen_placed=0
    def __init__(self,boardSize):
        self.boardSize=boardSize
        for i in range(0,boardSize):
            self.queenBoard.append(0)
        self.number_queen_placed=0
    
    def isQueenSafe(self,colNum):
        for i in range(0,self.number_queen_placed):
            if((self.queenBoard[i]==colNum) or abs(colNum-self.queenBoard[i])==(self.number_queen_placed-i)):
                return False
        return True
        
    def placeQueen(self,colNum):
        
        if(colNum>=0 and colNum < self.boardSize):
            self.queenBoard[self.number_queen_placed]=colNum
            self.number_queen_placed+=1
        else:
            print("Bad Column")
            
    def isFilled(self):
        if(self.number_queen_placed==self.boardSize):
            return True
        else:
            return False
    def unplaceQueen(self):
        if(self.number_queen_placed>0):
            self.number_queen_placed-=1
            

    def QueenDFS(self):
        if(self.isFilled()==True):
            return self.queenBoard
        else:
            for i in range(0,self.boardSize):
                if(self.isQueenSafe(i)):
                    self.placeQueen(i)
                    temp=NQueenSolution(0)
                    temp=self.QueenDFS()
                    if(not(temp is None)):
                        return temp
                    self.unplaceQueen()
        return None
                        
    def display(self):
        print(self.queenBoard,"placed are ")
        
        #***********************************************************************************
        #*********************************  NQueenSolution Class end Here *******************
        #**********************************************************************************
        
        
queen_input=[4,8,12,16,20,24,28]
processing_time=[]
for i in queen_input:
    #recording starting time of program
    start_time=time.clock()
    Sol1=NQueenSolution(i)
    Sol1.QueenDFS()
    processing_time.extend([time.clock()-start_time])
    Sol1.display()
    
# ploting the result

plotResult(queen_input,processing_time)