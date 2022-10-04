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
    csvData.plot.line(x="Time - Force(N)", y="F - Force(N)")
    plt.ylabel("Force (newtons)", size=16)
    plt.xlabel("Time (milliseconds)", size=16)
    plotName = namingPlotter(i)
    plt.title(plotName)
    plt.legend().remove()

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
    csvResistance.plot.line(x="Time - Plot 0", y="Amplitude - Plot 0")
    plt.ylabel("Amplitude (ohms)", size=16)
    plt.xlabel("Time (milliseconds)", size=16)
    plotName = namingPlotter(i)
    plt.title(plotName)
    plt.legend().remove()
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
    nameSeq = [0,0,0,0]
    fig, ax = plt.subplots(2,2,figsize=(8, 5))
    q=3
    for path in csvPaths[i-3:i+1]:
        
        if (("force" or "Force" ) in path and "0.5" in path):

            csvResistanceA = pd.read_csv(path)
            csvResistanceA.plot.line(ax=ax[0,1], x="Time - Force(N)", y="F - Force(N)", legend=None)
            nameSeq[1] = q

        if (("force" or "Force" ) in path and  "1N" in path):
            csvResistanceA = pd.read_csv(path)
            csvResistanceA.plot.line(ax=ax[0,0], x="Time - Force(N)", y="F - Force(N)", legend=None)
            nameSeq[0]=q

        if (("sensor" or "Sensor") in path and "0.5" in path):
           
            csvResistanceB = pd.read_csv(path)
            csvResistanceB.plot.line(ax=ax[1,1],x="Time - Plot 0", y="Amplitude - Plot 0",  legend=None)
            nameSeq[3] = q

        if (("sensor" or "Sensor") in path and "1N" in path):
           
            csvResistanceB = pd.read_csv(path)
            csvResistanceB.plot.line(ax=ax[1,0],x="Time - Plot 0", y="Amplitude - Plot 0",  legend=None)
            nameSeq[2] = q
        q-=1

    aPlotName = namingPlotter(i-nameSeq[0])
    bPlotName = namingPlotter(i-nameSeq[1])
    cPlotName = namingPlotter(i-nameSeq[2])
    dPlotName = namingPlotter(i-nameSeq[3])
    
    ax[0,0].set_title(aPlotName, fontsize=12)
    ax[0,1].set_title(bPlotName, fontsize=12)
    ax[1,0].set_title(cPlotName, fontsize=12)
    ax[1,1].set_title(dPlotName, fontsize=12)

    ax[0,0].set_xlabel('Time (miliseconds)', fontsize=10)
    ax[0,0].set_ylabel("Force (newtons)", fontsize=10)
    ax[0,1].set_xlabel('Time (miliseconds)', fontsize=10)
    ax[0,1].set_ylabel("Force (newtons)", fontsize=10)
    ax[1,1].set_xlabel(' ', fontsize=10)
    ax[1,1].set_ylabel("Amplitude (ohms)", fontsize=10)
    ax[1,0].set_xlabel(' ', fontsize=10)
    ax[1,0].set_ylabel("Amplitude (ohms)", fontsize=10)
    fig.tight_layout()
    try:

        plt.savefig(cwd+"/figures/" + aPlotName[:8] + ".png", dpi=1200)

    except:
        pass

    try:
        plt.savefig(cwd+"\\figures\\" + aPlotName[:8] + ".png", dpi=1200)

    except:
        print("save error. make sure the figures dir is in the same place as the python file.")

    plt.close()

def main():

    i = 0    
    for path in csvPaths:
        print(path)
        if (("force" or "Force") in path):
            
            forcePlotter(i)

        if (("sensor" or "Sensor") in path):
            
            resistancePlotter(i)
        if (i+1)%4 == 0:
            quadPlotter(i)
            
        i+=1


if __name__ == "__main__":
    cwd = os.getcwd()
    mainPath = input("Enter path to csv: ")
    csvPaths = csvFileLocator(mainPath)
    sys.exit(main())

