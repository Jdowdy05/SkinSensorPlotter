"""
This is used to create good looking plots for our recorded data on sensors :) 



@author: Jordan Dowdy 
@version: 1.0.0, 9/29/22


"""
import os
from unicodedata import name
import pandas as pd
import matplotlib.pyplot as plt
import sys
import chardet




def csvFileLocator(csvDir : str) -> "list[str]":                             

    pathList=[]
    nameList=[]

    if  not csvDir:
        csvDir = "."

    for root, dirs, files in os.walk(csvDir, topdown=True):
        for name in files:
            #if name.endswith(".gz") and name.startswith("lsst_a_"):
            if name.endswith(".csv"):
                pathList.append(os.path.join(root, name))
                #name, fits, gz = name.split(".")
                name, csv = name.split(".csv")
                nameList.append(name)
                print(nameList)
                print(pathList)

    return pathList, nameList


def forcePlotter(fileName : str, x: int):
    csvData = pd.read_csv(csvPaths[x])
    #print(csvData)
    csvData.plot.scatter(x="Time - Force(N)", y="F - Force(N)", alpha=0.5)
    plt.ylabel("Force (newtons)", size=16)
    plt.xlabel("Time (milliseconds)", size=16)
    print(fileName)
    plt.show()

def resistancePlotter(fileName : str, x: int):
    #rawdata = open(csvPaths[x], 'rb').read()
    #result = chardet.detect(rawdata)
    #charenc = result['encoding']
    #print(charenc)
    print(csvPaths[x])
    csvResistance = pd.read_csv("/Volumes/USB_DRIVE/Jordan/1layer/A/0.5-2Nsensorresponse9-23-2022.csv", encoding="Windows-1252")
    print(csvResistance)
    csvResistance.plot.scatter(x="Time - Plot 0", y="Amplitude - Plot 0", alpha=0.5)
    plt.ylabel("Force (newtons)", size=16)
    plt.xlabel("Time (milliseconds)", size=16)
    print(fileName)
    plt.show()
    


def main():

    j = 0
    for i in csvNames:
        print(i)
        if ("force" in i):
            forcePlotter(i,j)

        if ("sensor" in i):
            
            resistancePlotter(i,j)

        j+=1


if __name__ == "__main__":
    csvPaths, csvNames = csvFileLocator("/Volumes/USB_DRIVE/Jordan")
    sys.exit(main())

