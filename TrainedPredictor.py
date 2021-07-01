import pandas as pd
import matplotlib.pyplot as plt

# Getting Data
df = pd.read_csv("trainedLine.csv")
Data = df.values.tolist()

x = input("Enter x: ")
print("Value of y: ", (Data[0][0]*int(x)+Data[0][1]))
