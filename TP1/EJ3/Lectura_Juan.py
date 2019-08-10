import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime

NOMBRE_CSV = "/Users/malemuller/Desktop/TC/TP1/EJ3/csvTest.csv" #RECIBIRLO CON LA DIRECCION!!!


#info = pd.read_csv(NOMBRE_CSV, names=['frec', 'amp', 'ph'], header = 0,  delimiter = ";",encoding = "utf-8", decimal= ",") #SI SE USA DECIMAL CON PUNTO, CAMBIAR!
info = pd.read_csv(NOMBRE_CSV, header = 0,  delimiter = ";",encoding = "utf-8", decimal= ",") #SI SE USA DECIMAL CON PUNTO, CAMBIAR!

print(info['Frec'])
print(info)
#info = info.sort_values(by='frec')#, ascending=True)
info.sort_values("Frec",axis='index', ascending=True, inplace = True, na_position ='last')
print(type(info['Frec']))

for i in range(len(info)):
   print("frecuencia: "+ str(info['Frec'][i]))

