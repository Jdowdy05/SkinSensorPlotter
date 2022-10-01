"""
This is used to create good looking plots for our recorded data on sensors :) 



@author: Jordan Dowdy 
@version: 1.0.0, 9/29/22


"""
import os
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


def forcePlotter(i: int):
    #plots the data of the force
    csvData = pd.read_csv(csvPaths[i])
    #print(csvData)
    csvData.plot.scatter(x="Time - Force(N)", y="F - Force(N)", alpha=0.5)
    plt.ylabel("Force (newtons)", size=16)
    plt.xlabel("Time (milliseconds)", size=16)
    plotName = namingPlotter(i)
    plt.title(plotName)

    try:

        plt.savefig(cwd+"/figures/" + plotName + ".png", dpi=1200)

    except:
        pass

    try:
        plt.savefig(cwd+"\\figures\\" + plotName + ".png", dpi=1200)

    except:
        print("save error. make sure the figures dir is in the same place as the python file.")

    plt.close()

def resistancePlotter(i: int):
    #plots the data for the skin sensor
    csvResistance = pd.read_csv(csvPaths[i])
    #print(csvResistance)
    csvResistance.plot.scatter(x="Time - Plot 0", y="Amplitude - Plot 0", alpha=0.5)
    plt.ylabel("Amplitude (ohms)", size=16)
    plt.xlabel("Time (milliseconds)", size=16)
    plotName = namingPlotter(i)
    plt.title(plotName)
    try:

        plt.savefig(cwd+"/figures/" + plotName + ".png", dpi=1200)

    except:
        pass

    try:
        plt.savefig(cwd+"\\figures\\" + plotName + ".png", dpi=1200)

    except:
        print("save error. make sure the figures dir is in the same place as the python file.")

    plt.close()

def namingPlotter(x : int) -> str:
    #finds the name of file to properly name plot
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

def quadPlotter(i: int):
    #this is to plot all four of a type onto one plot

    #still needs work

    fig, ax = plt.subplots(2,2)
    
    csvResistanceA = pd.read_csv(csvPaths[i-3])
    aPlot = csvResistanceA.plot.scatter(x="Time - Force(N)", y="F - Force(N)", alpha=0.5)
    csvResistanceB = pd.read_csv(csvPaths[i-2])
    bPlot = csvResistanceB.plot.scatter(x="Time - Force(N)", y="F - Force(N)", alpha=0.5)
    csvResistanceC = pd.read_csv(csvPaths[i-1])
    cPlot = csvResistanceC.plot.scatter(x="Time - Plot 0", y="Amplitude - Plot 0", alpha=0.5)
    csvResistanceD = pd.read_csv(csvPaths[i])
    dPlot = csvResistanceD.plot.scatter(x="Time - Plot 0", y="Amplitude - Plot 0", alpha=0.5)
    ax[0,0].plot(aPlot)
    ax[0,1].plot(bPlot)
    plt.show()

def main():

    i = 0
    for path in csvPaths:
        print(path)
        if (("force" or "Force") in path):
            forcePlotter(i)

        if (("sensor" or "Sensor") in path):
            
            resistancePlotter(i)
        if (i+1)%4 == 0:
            #quadPlotter(i)
            pass
        i+=1


if __name__ == "__main__":
    cwd = os.getcwd()
    mainPath = input("Enter path to csv: ")
    csvPaths = csvFileLocator(mainPath)
    sys.exit(main())

