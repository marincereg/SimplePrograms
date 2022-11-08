# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:53:30 2022

@author: marin
Name : Path Algorithm
"""
import numpy as np
import pandas as pd

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
    def SearchNode (MatrixOfDistances, PathArray, DistanceArray ):
        cnt = 0
        cnt_2= 0
        NewPathArray = []
        NewPathArrayTemp = []
        NewDistanceArray = []
        #print (PathArray)
        for j in PathArray:
            if type(j)== list:
                j = j[-1]
            for i in range(0,len(MatrixOfDistances[1,:])):
                if DistanceMatrix[j,i] > 0:
                    if i not in PathArray[cnt_2]:
                        #print (i , PathArray[cnt_2] )
                        #print (PathArray)
                        NewPathArrayTemp.append([PathArray[cnt_2]])
                        NewPathArrayTemp[[cnt][0]].append([i])
                        NewPathArray.append( (NewPathArrayTemp[cnt][0]) + (NewPathArrayTemp[cnt][1]))
                        NewDistanceArray.append(DistanceArray[cnt_2]+MatrixOfDistances[j,i])
                        cnt = cnt + 1
            cnt_2 = cnt_2 + 1
        return (NewPathArray,NewDistanceArray)
    PathSolution = []
    DistanceSolution = []
    Start = [[Start]]
    Distance = [0]
    
    PathArray = Start.copy()
    DistanceArray = Distance.copy()
    
    BestDistance = 99_999
    StopLoop = False
    while StopLoop==False:
        PathArray,DistanceArray = SearchNode(MatrixOfDistances,PathArray,DistanceArray)
        poped = 0
        for i in range(0,len(PathArray)):
            if End in PathArray[i-poped]:

                if DistanceArray[i-poped] < BestDistance:
                    PathSolution=(PathArray[i-poped])
                    DistanceSolution=(DistanceArray[i-poped])
                    BestDistance = DistanceSolution
                #PathSolution.append(PathArray[i-poped])
                PathArray.pop(i-poped)            
                #DistanceSolution.append(DistanceArray[i-poped])
                DistanceArray.pop(i-poped)
                poped = poped + 1

        StopLoop = False
        for i in DistanceArray:
            if i>BestDistance and StopLoop==False:
                StopLoop = True

    return(PathSolution,DistanceSolution)



pa,ds = TravelAgentSearch(DistanceMatrix,0,18)

     
""" 
ShortestPath, Distance = GetShorthestPath_ComboMeth(DistanceMatrix,21,9)
print ("Shortest Path from " + Cities[21] + " To " + Cities[9])
for i in ShortestPath:
    print (Cities[i])
print ("With distance of : " + str(Distance) + " Milles" )
"""
ShortestPath, Distance = TravelAgentSearch(DistanceMatrix,0,18)
print ("Shortest Path from " + Cities[0] + " To " + Cities[18])
for i in ShortestPath:
    print (Cities[i])
print ("With distance of : " + str(Distance) + " Milles" )


        
        
        


