# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:53:30 2022

@author: marin
Name : Path Algorithm
"""
#import numpy as np
import pandas as pd
import time

# Get the data !
Data = pd.read_excel('Paths.xlsx')
Cities = Data.iloc[:,0]
DistanceMatrix_PD = Data.drop('City',axis=1)
DistanceMatrix = DistanceMatrix_PD.to_numpy()

def CheckIfAllAreUnique (*item):
    # Check if there is duplicate in given items
    # by default it all items are unique
    Unique = True
    if len(item) > 1:
        for i in range(0,len(item)):
            for j in range(i+1,len(item)):
                if item[i]==item[j]:
                    Unique = False
    return Unique

def CheckIfAllInArrayAreUnique (Array):
    # Check if there is duplicate in given items
    # by default it all items are unique
    Unique = True
    if len(Array) > 1:
        for i in range(0,len(Array)):
            for j in range(i+1,len(Array)):
                if Array[i]==Array[j]:
                    Unique = False
    return Unique

def GetDistance (MatrixOfDistances,PathNodes):
    # get distance in nodes using matrix of distance
    distance = 0
    StartNode = PathNodes[0]
    for i in PathNodes:
        distance = distance + MatrixOfDistances[StartNode,i]
        StartNode = i
    return distance

def GetShorthestPath_ComboMeth (MatrixOfDistances,Start,End):  
    # slowest algorithm - get all possible combination of path 
    def GetCombo(MatrixOfDistances,Start,End,Visited,CurBestDist):    
        # Get combination with parametest
        # start state
        # End State
        # Visited state generated outside of the function
        # CurBestDist is distance that is currently the best - if distance of current combination is starting to be greather, break function
        Combo = [Start]
        SearchState = Start
        VisitedStates = [Start] + Visited
        FoundNothing = False
        Distance = 0
        # while end is not finded or nothing is found in loop
        while End not in Combo and FoundNothing == False :
            FoundNothing = True
            for i in range(0,len(MatrixOfDistances[SearchState,:])):
                if MatrixOfDistances[SearchState,i] > 0:
                    # GetCombo found target state
                    if i == End:
                        Combo.append(i)
                        CurBestDist = Distance + MatrixOfDistances[SearchState,i]
                        VisitedStates.append(i)
                        SearchState = i
                        FoundNothing = False
                        break
                    # GetCombo still searching for target state
                    if i not in VisitedStates:
                        VisitedStates.append(i)
                        Distance = Distance + MatrixOfDistances[SearchState,i]
                        Combo.append(i)
                        SearchState = i     
                        FoundNothing = False
                # Current distance is greather than current minimal distance, Break
                if Distance >CurBestDist:
                    FoundNothing = True
                    Combo.clear()
                    break
            if FoundNothing == True:
                Combo.clear()
        return (Combo,CurBestDist) 
    """
    Function Logic
    """
    MinDistance = 99_999
    NewBestDistance = 99_999
    Path = []   
    NewBEstPath = []
    # Change Visited state - state that should be avoided so every iteration will posibly have new path
    for a in range(0,len(MatrixOfDistances[Start,:])):
        for b in range(0,len(MatrixOfDistances[Start,:])):
            for c in range(0,len(MatrixOfDistances[Start,:])):
                for d in range(0,len(MatrixOfDistances[Start,:])):
                    for e in range(0,len(MatrixOfDistances[Start,:])):
                        # Check if visited state are not start and end 
                        if [a,b,c,d,e] != [Start,End]:
                            VisitedState = [Start,a,b,c,d,e]
                            Path,MinDistance = GetCombo(MatrixOfDistances,Start,End,VisitedState,MinDistance)
                            # check current distance and current best distance and take what is better
                            if len(Path)>0:
                                # this is done because some iteration get curr distance + final and distance get overshooted but writen
                                if MinDistance > NewBestDistance:
                                    MinDistance = NewBestDistance
                                    Path = NewBEstPath
                                NewBestDistance = MinDistance
                                NewBEstPath = Path
    return (NewBEstPath,MinDistance)

def TravelAgentSearch (MatrixOfDistances,Start,End):
    # Travel Agent Algorithm
    # expand nodes and search for the best path until all possible paths are above best one 
    def SearchNode (MatrixOfDistances, PathArray, DistanceArray ):
        # search node returns the paths from given node
        # init phase
        cnt = 0
        cnt_2= 0
        NewPathArray = []
        NewPathArrayTemp = []
        NewDistanceArray = []
        # Function Loop - Search trought array
        for j in PathArray:
            # if j is array take last element in array
            if type(j)== list:
                j = j[-1]
            for i in range(0,len(MatrixOfDistances[1,:])):
                # get only i greather than 0 - possible path
                if DistanceMatrix[j,i] > 0:
                    # take one that will not repeat itself  - example (1-0-1)
                    if i not in PathArray[cnt_2]:
                        NewPathArrayTemp.append([PathArray[cnt_2]])
                        NewPathArrayTemp[[cnt][0]].append([i])
                        NewPathArray.append( (NewPathArrayTemp[cnt][0]) + (NewPathArrayTemp[cnt][1]))
                        NewDistanceArray.append(DistanceArray[cnt_2]+MatrixOfDistances[j,i])
                        cnt = cnt + 1
            # Cnt_2 is for the other PathArray that are found before and should be appended to finding a path
            cnt_2 = cnt_2 + 1
        return (NewPathArray,NewDistanceArray)
    # Main Loop of search algorithm
    # init phase
    PathSolution = []
    DistanceSolution = []
    Start = [[Start]]
    Distance = [0]
    PathArray = Start.copy()
    DistanceArray = Distance.copy()
    BestDistance = 99_999
    StopLoop = False  
    # Algorithm
    while StopLoop==False:
        # call search node
        PathArray,DistanceArray = SearchNode(MatrixOfDistances,PathArray,DistanceArray)
        # Check quality of search and discard what could be discarded
        poped = 0
        for i in range(0,len(PathArray)):
            if End in PathArray[i-poped]:
                # new best path !!! discard it from distance array
                if DistanceArray[i-poped] < BestDistance:
                    PathSolution=(PathArray[i-poped])
                    DistanceSolution=(DistanceArray[i-poped])
                    BestDistance = DistanceSolution
                PathArray.pop(i-poped)            
                DistanceArray.pop(i-poped)
                poped = poped + 1
            else:
                # if some path in distance array is passing current best path discard it too
                if DistanceArray[i-poped] > BestDistance:
                    PathArray.pop(i-poped)            
                    DistanceArray.pop(i-poped)
                    poped = poped + 1
        # Check if we are done - Checking if there is ANY path that currently have lover distance than best path    
        if BestDistance != 99_999:
            StopLoop = True
            for i in DistanceArray:
                if i < BestDistance:
                    StopLoop = False
    return(PathSolution,DistanceSolution)
     
#Search Parameters
StartNode = 0
EndNode = 18

# SLOW PATH FINDING ALGORITHM - APROX 1 min
t1 = time.time()
ShortestPath, Distance = GetShorthestPath_ComboMeth(DistanceMatrix,StartNode,EndNode)
t2 = time.time()
print ("Shortest Path from " + Cities[StartNode] + " To " + Cities[EndNode])
for i in ShortestPath:
    print (Cities[i])
print ("With distance of : " + str(Distance) + " Milles" )
print ("Path found in : " + str(t2-t1) + " Sec" )

print ("\n" )
# FAST PATH FINDING ALGORITHM - APROX >0.1 sec
t1 = time.time()
ShortestPath, Distance = TravelAgentSearch(DistanceMatrix,StartNode,EndNode)
t2 = time.time()
print ("Shortest Path from " + Cities[StartNode] + " To " + Cities[EndNode])
for i in ShortestPath:
    print (Cities[i])
print ("With distance of : " + str(Distance) + " Milles" )
print ("Path found in : " + str(t2-t1) + " Sec" )


        
        
        


