import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as Tk
from tkinter import filedialog
from datetime import datetime
from numpy.polynomial import Polynomial
import os
from dataclasses import dataclass
import mplcursors



# File Picker
Tk.Tk().withdraw() # prevents an empty tkinter window from appearing

filepath = filedialog.askopenfilename()
# print(filepath)

fileName = os.path.basename(filepath)
print(fileName)
# ******************************
#       Enter CSV File Name
# ******************************
csvFile = filepath

print("Creating graphs for: " + csvFile)
df = pd.read_csv(csvFile, encoding='ISO-8859-1', sep=',', usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])

print("\nWhat graph do you want to make?"
"\n1- Voltage vs current"
"\n2- power vs voltage"
"\n3- power vs time"
"\n4- power vs time graph + light"
"\n5- light vs time"
"\n6- power vs time graph + temperature"
"\n7- AOFA - power vs time graph + light"
"\n8- Voltage vs time")
graphNumber = input("Enter number: ")

print("\n\nRight click to place measurement"
"\n Left click to remove")

# Global Text size and font config
plt.rc('font', size=20) #Set font size
plt.rcParams["font.family"] = "Aptos" #Set font

#Create array of time that is in seconds instead of ms
x = df.iloc[:, 1] #X axis is col 1 (elapsed time)
xArray = np.array(x)
TimeSec = xArray / 1000

if(graphNumber.isnumeric()):
    match int(graphNumber):
        case 1:
            """ Create Voltage vs current graph """
            x = df.iloc[:, 2] #X axis is col 2
            y = df.iloc[:, 3] #Y axis is col 3

            # Trendline?
            # z = np.polyfit(x, y, 2)
            # p = np.poly1d(z)
            # plt.scatter(x,y)
            # plt.plot(x, p(x), "g-")  # 'g-' is for a green solid line

            fig, ax = plt.subplots()
            # ax.plot(x,y, c="#AC2B37")
            ax.scatter(x,y, marker= "^", c="#AC2B37")
            fig.set_size_inches(12, 8, forward=True)
            plt.xlabel("Voltage (V)")
            plt.ylabel("Current (A)")
            plt.title("Current vs Voltage")
            plt.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
            ax.minorticks_on()
            plt.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
            ax.set_ylim([0, 2.5])
            ax.set_xlim([0, 25])
            
        case 2:
            """ Create power vs voltage graph """
            x = df.iloc[:, 2] #X axis is col 2
            y = df.iloc[:, 4] #Y axis is col 4

            # Trendline?
            # z = np.polyfit(x, y, 2)
            # p = np.poly1d(z)
            # plt.scatter(x,y)
            # plt.plot(x, p(x), "g-")  # 'g-' is for a green solid line

            fig, ax = plt.subplots()
            ax.scatter(x,y, marker= "^", c="#AC2B37")
            fig.set_size_inches(12, 8, forward=True)
            plt.xlabel("Voltage (V)")
            plt.ylabel("Power (W)")
            plt.title("Power vs Voltage")
            plt.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
            ax.minorticks_on()
            plt.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
            # ax.set_ylim([0, 30])
        case 3:
            """ Create power vs time graph """
            x = TimeSec
            y = df.iloc[:, 4] #Y axis is col 4

            # Trendline?
            # z = np.polyfit(x, y, 2)
            # p = np.poly1d(z)
            # plt.scatter(x,y)
            # plt.plot(x, p(x), "g-")  # 'g-' is for a green solid line

            fig, ax = plt.subplots()
            ax.plot(x,y, c="#AC2B37")
            ax.scatter(x,y, marker= "^", c="#AC2B37")
            fig.set_size_inches(12, 8, forward=True)
            plt.xlabel("Time (S)")
            plt.ylabel("Power (W)")
            plt.title("Power vs Time")
            plt.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
            ax.minorticks_on()
            plt.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
            ax.set_ylim([0, 30])
        case 4:
            """ Create power vs time graph + light over time """
            x = TimeSec
            y = df.iloc[:, 4] #Y axis is col 4 (POWER)
            z = df.iloc[:, 12] #Y2 axis, is col 12 (LIGHT)

            fig, ax = plt.subplots()
            ax2 = ax.twinx()
            Power, = ax.plot(x,y, c="#AC2B37", label = "Power")
            ax.scatter(x,y, marker= "^", c="#AC2B37")
            Light, = ax2.plot(x,z, c="#003f5c", label = "Light")
            fig.set_size_inches(12, 8, forward=True)
            ax.set_xlabel("Time (S)")
            ax.set_ylabel("Power (W)")
            ax2.set_ylabel("Light (W/m^2)")
            plt.title("Power and Light vs Time - " + fileName)
            ax.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
            ax.minorticks_on()
            ax2.minorticks_on()
            ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
            ax.set_ylim([0, 30])
            ylim = ax2.get_ylim()
            ylim = ylim[1] * (1.1)
            ax2.set_ylim(bottom = 0, top = ylim)
            # Function add a legend
            plt.legend(handles = [Power, Light], loc="center left")
        case 5:
            """ Create light vs time graph """
            x = TimeSec
            y = df.iloc[:, 12] #Y axis is col 12

            # Trendline?
            # z = np.polyfit(x, y, 2)
            # p = np.poly1d(z)
            # plt.scatter(x,y)
            # plt.plot(x, p(x), "g-")  # 'g-' is for a green solid line

            fig, ax = plt.subplots()
            ax.plot(x,y, c="#AC2B37")
            fig.set_size_inches(12, 8, forward=True)
            plt.xlabel("Time (S)")
            plt.ylabel("Light (W/m^2)")
            plt.title("Light vs Time")
            plt.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
            ax.minorticks_on()
            plt.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
            # ax.set_ylim([0, 1300])
        case 6:
            """ Create power vs time graph + temperature over time TMP ONLY****** """
            x = TimeSec
            y = df.iloc[:, 4] #Y axis is col 4 (POWER)
            z = df.iloc[:, 11] #Y2 axis, is col 11 (TEMP)

            fig, ax = plt.subplots()
            ax2 = ax.twinx()
            Power, = ax.plot(x,y, c="#AC2B37", label = "Power")
            ax.scatter(x,y, marker= "^", c="#AC2B37")
            Light, = ax2.plot(x,z, c="#003f5c", label = "Temperature")
            fig.set_size_inches(12, 8, forward=True)
            ax.set_xlabel("Time (S)")
            ax.set_ylabel("Power (W)")
            ax2.set_ylabel("Temperature (°C)")
            plt.title("Power and Temperature vs Time")
            ax.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
            ax.minorticks_on()
            ax2.minorticks_on()
            ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
            ax.set_ylim([0, 30])
            ylim = ax2.get_ylim()
            ylim = ylim[1] * (1.1)
            ax2.set_ylim(bottom = 0, top = ylim)
            # Function add a legend
            plt.legend(handles = [Power, Light], loc="center left")
        case 7:
            # Define vars to represent algorithms
            CV= 0
            B= 1
            PNO= 2
            PNOV= 3
            INC= 4
            INCV= 5
            PSO= 6
            TMP= 7

            startFlag = True
            # List to store all info for graphing sections
            algoSections = []
            # Create custom AofA graph with highted sections
            """ Create power vs time graph + light over time """
            x = TimeSec
            y = df.iloc[:, 4] #Y axis is col 4 (POWER)
            z = df.iloc[:, 12] #Y2 axis, is col 12 (LIGHT)

            # Determine where to create the colors
            algo = df.iloc[:, 14] #Algo is in col 14
            oldAlgoNum = -1
            algoNum = -1
            for index, algoName in enumerate(algo):
                algoName = algoName.strip()
                match algoName:
                    case "CV":
                        algoNum = CV
                        color = "#007ab1"
                    case "B":
                        algoNum = B
                        color = "#637bc9"
                    case "PNO":
                        algoNum = PNO
                        color = "#ac73c9"
                    case "PNOV":
                        algoNum = PNOV
                        color = "#e967b1"
                    case "INC":
                        algoNum = INC
                        color = "#ff6685"
                    case "PSO":
                        algoNum = PSO
                        color = "#ff7f50"
                    case "TMP":
                        algoNum = TMP
                        color = "#ffa600"

                if algoNum != oldAlgoNum:
                    if startFlag == True: #If just starting 
                        # Algo has changed, record index value as a new start
                        algoSections.append(dict(start = index, algo = algoName, color = color))
                        oldAlgoNum = algoNum
                        startFlag = False
                    else:
                        # Algo has changed, record PREVIOUS index value as the end
                        # grab last item on the dict and add the end index
                        algoSections[-1]["end"] = index-1
                        
                        #Now deal with the current new start
                        algoSections.append(dict(start = index, algo = algoName, color = color))
                        oldAlgoNum = algoNum

            fig, ax = plt.subplots()
            ax2 = ax.twinx()
            Power, = ax.plot(x,y, c="#AC2B37", label = "Power")
            ax.scatter(x,y, marker= "^", c="#AC2B37")
            Light, = ax2.plot(x,z, c="#003f5c", label = "Light")
            fig.set_size_inches(12, 8, forward=True)
            ax.set_xlabel("Time (S)")
            ax.set_ylabel("Power (W)")
            ax2.set_ylabel("Light (W/m^2)")
            plt.title("Power and Light vs Time")
            ax.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
            ax.minorticks_on()
            ax2.minorticks_on()
            ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
            ax.set_ylim([0, 30])
            ylim = ax2.get_ylim()
            ylim = ylim[1] * (1.1)
            ax2.set_ylim(bottom = 0, top = ylim)

            # Add in custom shaded sections
            algoHandles = []
            listOfAlgos = []

            # need to fix the last section to add the end point as the end of the recorded time
            algoSections[-1]["end"] = -1 # set index to end of time array

            for index, algoDict in enumerate(algoSections):
                # check if algo name is in the list yet to plot them on the legend only once
                label = "_nolegend_" # Label will be _nolegend_, preventing it from showing on the legend
                if algoDict.get("algo") not in listOfAlgos:
                    label = algoDict.get("algo")
                    listOfAlgos.append(algoDict.get("algo")) # add name to list if it is unique
                    
                # get x values in time array and color from algoDict and make a colored area with 10% transparency
                algoHandles.append(ax.axvspan(TimeSec[algoDict.get("start")], TimeSec[algoDict.get("end")], facecolor=algoDict.get("color"),
                alpha=0.1, label= label))


            # Create seperate color legend
            first_legend = ax.legend(handles = algoHandles, loc='best', framealpha = 0.5)
            ax.add_artist(first_legend)

            # Function add a legend
            plt.legend(handles = [Power, Light], loc="lower right")

        case 8:
            """ Create voltage vs time graph """
            x = TimeSec
            y = df.iloc[:, 2] #Y axis is col 2


            fig, ax = plt.subplots()
            ax.plot(x,y, c="#AC2B37")
            ax.scatter(x,y, marker= "^", c="#AC2B37")
            fig.set_size_inches(12, 8, forward=True)
            plt.xlabel("Time (S)")
            plt.ylabel("Voltage (V)")
            plt.title("Voltage vs Time")
            plt.grid(which='major', linestyle='-', linewidth=1, alpha=0.8)
            ax.minorticks_on()
            plt.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.8)
            # ax.set_ylim([0, 30])


# ENABLE POINT SELECTION AND SHOW PLOT
mplcursors.cursor(multiple=True)
plt.show()


# Column format (starts at 0)
# Timestamp, Elapsed Time, PM1 (V), PM1(I), PM1(W), PM2 (V), PM2(I), PM2(W), PM3 (V), PM3(I), PM3(W), Temp (C), Light (W/m^2), Duty, Algorithm

