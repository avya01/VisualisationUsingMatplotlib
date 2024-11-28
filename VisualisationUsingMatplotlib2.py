import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("Company Sales Data.csv")

plt.plot(file.month_number, file.facecream, marker="o", linewidth=3)
plt.plot(file.month_number, file.facewash, marker="o", linewidth=3)
plt.plot(file.month_number, file.toothpaste, marker="o", linewidth=3)
plt.plot(file.month_number, file.bathingsoap, marker="o", linewidth=3)
plt.plot(file.month_number, file.shampoo, marker="o", linewidth=3)
plt.title("Units of all products")
plt.xlabel("Month")
plt.ylabel("Total Units")
plt.legend(["Facecream","Facewash", "Toothpaste", "Bathing Soap", "Shampoo"])
plt.show()