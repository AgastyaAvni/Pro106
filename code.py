import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath):

   week=[]
   Coffee in ml=[]

    with open(dataPath) as f:
        df=csv.DictReader(f)
        for row in df:
            iceCreamSales.append(float(row['week']))
            coldDrinkSales.append(float(row['Coffee in ml']))

    return{'x':week,'y':Coffee in ml}

def findCoRelation(DataSource):
    correlation=np.corrcoef(DataSource['x'],DataSource['y'])
    print('Correlation between Week and Coffe sales : \n-->',correlation[0,1])

def setup():
    dataPath='data.csv'
    DataSource=getDataSource(dataPath)
    findCoRelation(DataSource)

setup()
        




