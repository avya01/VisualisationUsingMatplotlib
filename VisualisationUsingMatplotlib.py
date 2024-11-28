import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("Company Sales Data.csv")

plt.plot(file.month_number, file.total_profit, linestyle="dotted", marker="o", mec="red", linewidth=3, color="black")
plt.title("Profits per month")
plt.xlabel("Month")
plt.ylabel("Total_profits")
plt.show()