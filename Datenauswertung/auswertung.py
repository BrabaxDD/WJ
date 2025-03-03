import pandas as pd
import matplotlib.pyplot as plt


data = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [],
        10: [], 11: [], 12: [], 12: [], 13: [], 14: [], 15: [], 16: [],}

with open("20250225_SH2_2.dat", "r") as file:
    for line in file:
        measurments = line.strip().split()
        for i, measurment in enumerate(measurments):
            data[i].append(float(measurment))



#print(data[0])
#print(data[1])
toplotRelative = []
toplotDiffrence = []
toplotAbsolute = []
df = pd.DataFrame(data)
for i,measurement in enumerate(df):
    if i != 0 and i not in [1,2,3,4,9,14,15,16]:

    #if i != 0 and i not in [1,2,3,14,16]:
        origin = df[i][:2000].mean()
        df["rolling" + str(i)] = df[i].rolling(window=800).mean()
        df["rollingRelative" + str(i)] = df["rolling" + str(i)] / origin
        df["rollingDiffrence"+str(i)] = df["rolling"+str(i)] - origin
        toplotRelative.append("rollingRelative" + str(i))
        toplotDiffrence.append("rollingDiffrence" + str(i))
        toplotAbsolute.append("rolling"+str(i))
#        df.plot(x=0,y=("rollingRelative" + str(i)), kind = "line")

df.plot(x = 0,y=toplotRelative,kind="line",xlabel="Zeit in Millisekunden",ylabel="relativer Widerstand")
df.plot(x = 0,y=toplotDiffrence,kind="line",xlabel="Zeit in Millisekunden",ylabel="Widerstands Different in Ohm")
df.plot(x = 0,y=toplotAbsolute,kind="line",xlabel="Zeit in Millisekunden",ylabel="Widerstand in Ohm")


plt.show()



        #df.plot(x=0, y="rolling4", kind="line")
