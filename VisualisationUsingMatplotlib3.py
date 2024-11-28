import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("Company Sales Data.csv")

plt.bar(file.month_number, file.facecream)
plt.bar(file.month_number, file.facewash)
plt.title("Sales of facecream compared to facewash")
plt.xlabel("Month")
plt.ylabel("Number of Sales")
plt.legend(["Facecream", "Facewash"])
plt.show()