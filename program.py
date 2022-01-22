import csv
import plotly.express as px
import numpy as np

def plotFigure(data_path):
    with open("data.csv", newline='') as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
        fig.show()

def getDataSource(data_path):
    Coffee = []
    Sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee.append(float(row["Cofee in ml"]))
            Sleep.append(float(row["sleep in hours"]))
    
    return {"x": Coffee, "y": Sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("The correlation between coffee drank in ml and sleep in hours is", correlation[0,1])

def setup():
    data_path = "data.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)