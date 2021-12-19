import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("total_stars.csv")

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()

mass.sort()
radius.sort()


plt.plot(radius,mass)

plt.title("Radius & Mass of the Star")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass,radius)

plt.title("Mass vs Radius")
plt.xlabel("Mass")
plt.show()

plt.scatter(radius,mass)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()