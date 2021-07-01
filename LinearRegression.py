import pandas as pd
import random
import matplotlib.pyplot as plt

# Getting Data
df = pd.read_csv("Data.csv")
Data = df.values.tolist()

# Variables and constants
alpha = 0.0000001
h = 0.02
# This range is given to keep the program stable keeping in mind ground truth value, but this should be removed to make a perfectly generic program.
m = random.randrange(-4, 6)
print("Initial m: ", m)
c = random.randrange(-5, 5)  # Same reason as above
print("Initial c: ", c)
mDash = m  # m'
cDash = c  # c'
signFlipped = False
dldm = 0  # dl/dm
dldc = 0  # dl/dc

# Iteration until convergence of m and c
for (i) in range(0, 100):

    # calculate dl/dm and m'
    mLossOne = 0
    for(x) in range(0, len(Data)):
        # (ti-((m+h)x+c))^2
        mLossOne += ((Data[x][1])-((((m+h)*x)+c)*(((m+h)*x)+c)))
    mLossTwo = 0
    for(x) in range(0, len(Data)):
        mLossTwo += ((Data[x][1])-(((m*x)+c)*((m*x)+c)))  # (ti-(mx+c))^2
    mDash = m - alpha*((mLossOne-mLossTwo)/h)  # m'= m - alpha(dl/dm)

    # Check if dl/dm flipped signs this iteration
    if(((mLossOne-mLossTwo)/h >= 0 and dldm < 0 and i != 0) or ((mLossOne-mLossTwo)/h < 0 and dldm >= 0 and i != 0)):
        signFlipped = True

    # calculate dl/dc and c'
    cLossOne = 0
    for(x) in range(0, len(Data)):
        # (ti-(mx+(c+h)))^2
        cLossOne += ((Data[x][1])-(((m*x)+(c+h))*((m*x)+(c+h))))
    cLossTwo = 0
    for(x) in range(0, len(Data)):
        cLossTwo += ((Data[x][1])-(((m*x)+c)*((m*x)+c)))  # (ti-(mx+c))^2
    cDash = c - alpha*((cLossOne-cLossTwo)/h)  # c'= c - alpha(dl/dc)

    # Check if dl/dc flipped signs this iteration
    if(((cLossOne-cLossTwo)/h >= 0 and dldc < 0 and i != 0) or ((cLossOne-cLossTwo)/h < 0 and dldc >= 0 and i != 0)):
        signFlipped = True

    # Changing values for next iteration
    if signFlipped == True:
        alpha = alpha/2
        signFlipped = False
    print("ITERATION ", i)
    m = mDash
    print(" m: ", m)
    c = cDash
    print(" c: ", c)
    dldm = (mLossOne-mLossTwo)/h
    dldc = (cLossOne-cLossTwo)/h

print("FINAL: ")
print("m: ", round(m, 4))
print("c: ", round(c, 4))

# Saving trained values of m and c
trainedLine = [(m, c)]
df = pd.DataFrame(trainedLine)
df.to_csv("trainedLine.csv", index=False)


# Plotting:

# Actual data
x = [x[0] for x in Data]
y = [y[1] for y in Data]
plt.scatter(x, y)

# Our model
model = []
for(x) in range(1, 11):
    print("x", x, "=", x, ", y", x, "=", (m*x)+c)
    model.append((x, ((m*x)+c)))
x = [x[0] for x in model]
y = [y[1] for y in model]
plt.plot(x, y)

# Graph stuff
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Datapoints vs Model line')
plt.show()
