import random
import pandas as pd
import matplotlib.pyplot as plt

# Ground truth line. m=1, c=0
coordinatesArray = []

# Randomizing y coordinates
for(x) in range(1, 11):
    coordinatesArray.append((x, x+(random.randrange(-1, 1))/4))


# Saving Data to CSV file
df = pd.DataFrame(coordinatesArray)
df.to_csv("Data.csv", index=False)
