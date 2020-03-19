import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

style.use("ggplot")

df2 = pd.read_csv("E:\\Padhai\\Programming\\QShore\\Pandas\\train.csv")

x = df2.PassengerId[10:50]
y = df2.Fare[10:50]
plt.subplot(311)
plt.plot(x,y,label='Line',color="green")
plt.title("Cost Fluctuation")
#plt.xlabel("Passenger")
plt.ylabel("Fare")
plt.legend()
plt.grid(True,color="red")
plt.subplot(312)
plt.bar(x,y,label='Bar',color="blue")
#plt.title("Cost Fluctuation")
plt.xlabel("Passenger")
plt.ylabel("Fare")
plt.legend()
plt.grid(True,color="red")
plt.subplot(313)
plt.scatter(x,y,label='SCatter Plot',color="purple")
#plt.title("Cost Fluctuation")
plt.xlabel("Passenger")
plt.ylabel("Fare")
plt.legend()
plt.grid(True,color="red")

plt.show()

