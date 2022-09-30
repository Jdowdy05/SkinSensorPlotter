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





def csvFileLocator(csvDir : str) -> "list[str]":                             

    pathList=[]

    if  not csvDir:
        csvDir = "."

    for root, dirs, files in os.walk(csvDir, topdown=True):
        for name in files:
            #if name.endswith(".gz") and name.startswith("lsst_a_"):
            if name.endswith(".csv"):
                if name.startswith("._"):
                    continue
                pathList.append(os.path.join(root, name))
    



    return pathList


def forcePlotter( x: int):
    csvData = pd.read_csv(csvPaths[x])
    #print(csvData)
    csvData.plot.scatter(x="Time - Force(N)", y="F - Force(N)", alpha=0.5)
    plt.ylabel("Force (newtons)", size=16)
    plt.xlabel("Time (milliseconds)", size=16)
    plotName = namingPlotter(x)
    plt.title(plotName)
    plt.savefig(cwd+"/figures/" + plotName + ".png", dpi=1200)
    plt.close()

def resistancePlotter(x: int):
    csvResistance = pd.read_csv(csvPaths[x], encoding="Windows-1252")
    #print(csvResistance)
    csvResistance.plot.scatter(x="Time - Plot 0", y="Amplitude - Plot 0", alpha=0.5)
    plt.ylabel("Amplitude (ohms)", size=16)
    plt.xlabel("Time (milliseconds)", size=16)
    plotName = namingPlotter(x)
    plt.title(plotName)
    plt.savefig(cwd+"/figures/"+ plotName + ".png", dpi=1200)
    plt.close()
def namingPlotter(x : int) -> str:
    
    sensorType = csvPaths[x].replace(mainPath, "")
    
    plotName = sensorType.replace("/", "-")
    plotName = plotName.replace(".csv", "")
    if plotName[0:1] == "-":
        plotName = plotName[1:]
    try:
        plotName = plotName.replace(".tmp", "")

    except:
        pass
    return plotName

def main():

    j = 0
    for i in csvPaths:
        print(i)
        if (("force" or "Force") in i):
            forcePlotter(j)

        if (("sensor" or "Sensor") in i):
            
            resistancePlotter(j)

        j+=1


if __name__ == "__main__":
    cwd = os.getcwd()
    mainPath = input("Enter path to csv: ")
    csvPaths = csvFileLocator(mainPath)
    sys.exit(main())

