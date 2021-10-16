#!/bin/python3

import pygal

instructions = print("This program only accepts lowercase letters")

pie_chart = input ("Do you want a pie chart? ")

if pie_chart == "yes":     # PIE_CHART
    piechart2 = pygal.Pie()
    your_file = input ("Write here your file:  ")
    file = open (your_file, "r")

    for line in file.read().splitlines():
        if line:
            label, value = line.split(" ")
            piechart2.add(label, int(value))
       
    file.close()

    piechart2.render() 
elif pie_chart == "no":
    bar_chart = input ("Do you want a bar chart? ")
    if bar_chart == "yes":    # BAR_CHART
        barchart = pygal.Bar()

        your_file = input ("Write here your file:  ")
        file = open (your_file, "r")

        for line in file.read().splitlines():
            if line:
                label, value = line.split(" ")
                barchart.add(label, int(value))
       
                file.close()

                barchart.render()
    elif bar_chart == "no":
        error = input("We have nothing else.")
    else:
        error1 = input("Please try it again")
else:
    input("Try it again because something is wrong")
