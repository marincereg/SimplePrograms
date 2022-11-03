# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 20:26:52 2022

@author: marin
Name : Log Creator
"""
import datetime

def SW_InRun ():
    current_time = datetime.datetime.now()
    with open("Log.txt", "a") as LogFile:
        LogFile.write("\n")
        LogFile.write("[SW STARTED] "+ str(current_time) + "\n")
def Log_Warning (ErrorMSG):
    current_time = datetime.datetime.now()
    with open("Log.txt", "a") as LogFile:
        LogFile.write("[WARNING] "+ str(current_time) +"---" + ErrorMSG + "\n")
def Log_Fault (FaultMSG):
    current_time = datetime.datetime.now()
    with open("Log.txt", "a") as LogFile:
        LogFile.write("[FAULT] "+ str(current_time) +"---" + FaultMSG + "\n")
        LogFile.write("\n")



