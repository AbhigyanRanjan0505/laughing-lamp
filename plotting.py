import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("final.csv")

mass_list = df["Mass_Star"].tolist()
mass_list.pop(0)

radius_list = df["Radius_Star"].tolist()
radius_list.pop(0)

gravity_list = df["Gravity"].tolist()
gravity_list.pop(0)

plt.figure()
sns.scatterplot(x=mass_list, y=radius_list)
plt.title("Star Mass and Radius")
plt.xlabel("Mass")
plt.ylabel("Radius")
plt.show()

plt.figure()
sns.scatterplot(x=mass_list, y=gravity_list)
plt.title("Star Mass and Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()
