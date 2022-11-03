# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 20:14:33 2022
@author: marin
Name : Test the Sorting Algorithm
"""
import time
import random
import LogCreator
import SortingAlgorithms

def GetArray (NumOfItems,Range,ArrPref):
    # NumOfItems in parameter for number of items in array
    # Range is parameter geting maximum value in array (from 0 to Range)
    # ArrPref is parameter that will: 0-create default random array, 1- rising sorted array, 2- falling sorted array
    Array = []
    Check = True
    try:
        if NumOfItems < 1: # check if number of items is low
            LogCreator.Log_Fault("Array with ONLY one item")
            Check = False
        if Range < 2 : # check if range is low
            LogCreator.Log_Warning("Array with ONLY two possible values")
        if Check :
            for i in range(0,NumOfItems):
                Array.append(random.randint(0,Range))
            if ArrPref == 1:
                Array.sort()
            if ArrPref == 2:
                Array.sort(reverse=True)
    #If error occur
    except:
        LogCreator.Log_Fault("Wrong input parameters !")
    return Array

def CheckQualityOfSort (LetsCalledSortedArray) :
    TestPassed = 0
    for i in range(0,len(LetsCalledSortedArray)-2):
        if LetsCalledSortedArray[i]<=LetsCalledSortedArray[i+1]:
            TestPassed = TestPassed + 1
    if TestPassed == len(LetsCalledSortedArray)-2:
        print ("Sorting was done sucessfuly")
    else:
        print ("Test Failed !! Test score : " + str(TestPassed/(len(LetsCalledSortedArray)-2)*100))

def TestSortingMethod (Function,ArrayToSort) :
    try:
        t0 = time.time()
        SortedArray = Function(ArrayToSort)
        t1 = time.time()
        return SortedArray,(t1-t0)
    except:
        LogCreator.Log_Fault("Could not Sort the array")

# Log that Sw is started
LogCreator.SW_InRun()
# Create Array
Array = GetArray(10_000,99_999,0)
#Copy test array so test arrays will be same
Array_1 = Array.copy()
Array_2 = Array.copy()
Array_3 = Array.copy()

# Sort with given methods - Call SorthinAlgorithm 
Sorted_1,time_1 = TestSortingMethod(SortingAlgorithms.BubleSort,Array_1)
Sorted_2,time_2 = TestSortingMethod(SortingAlgorithms.CocktailShaker,Array_2)
Sorted_3,time_3 = TestSortingMethod(SortingAlgorithms.QuickSort,Array_3)

# Check quality of sorting
CheckQualityOfSort(Sorted_1)
CheckQualityOfSort(Sorted_2)
CheckQualityOfSort(Sorted_3)





            
                                     
        
        

        

        
        
    
    

