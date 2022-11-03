# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 20:13:34 2022

@author: marin
Name : Sorthing algorithm
"""
def BubleSort (ArrayToSort):
    # As bubble get biggest value at the top and reduce end of the array by 1 until sorted
    DoneNo = 0
    while (DoneNo <= len(ArrayToSort)):
        for i in range(0,len(ArrayToSort)-DoneNo-1):
            if ArrayToSort[i] > ArrayToSort[i+1]:
                ArrayToSort[i],ArrayToSort[i+1] = ArrayToSort[i+1], ArrayToSort[i]
        DoneNo = DoneNo + 1
    return ArrayToSort

def CocktailShaker (ArrayToSort_2):
    # Similar to BubleSOrt, just as cocktail shake move biggest up and lowest down until sorted
    def CocktailShakerAlgorithm (ArrayToSort_2,LowDone,HighDone):
        for i in range(LowDone,len(ArrayToSort_2)-HighDone-1):
            if ArrayToSort_2[i] > ArrayToSort_2[i+1]:
                ArrayToSort_2[i],ArrayToSort_2[i+1] = ArrayToSort_2[i+1], ArrayToSort_2[i]
        HighDone = HighDone + 1
        for i in range(len(ArrayToSort_2)-HighDone-1,LowDone,-1):
            if ArrayToSort_2[i] < ArrayToSort_2[i-1]:
                ArrayToSort_2[i],ArrayToSort_2[i-1] = ArrayToSort_2[i-1], ArrayToSort_2[i]
        LowDone = LowDone + 1
        return (ArrayToSort_2,LowDone,HighDone)
    High = 0
    low = 0
    while low < len(ArrayToSort_2)-High :
        ArrayToSort_2,High,low = CocktailShakerAlgorithm(ArrayToSort_2,low,High)
    return ArrayToSort_2

def QuickSort (ArrayToSort):
    # quick sort patern divide array around pivot and swithc all values bigger/smaller around pivot. keep doing that until sorted
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1
    def quickSort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quickSort(array, low, pi - 1)
            quickSort(array, pi + 1, high)
    quickSort(ArrayToSort, 0, len(ArrayToSort)-1)
    return ArrayToSort

