import matplotlib.pyplot as plt 

values = [409, 242, 385, 238, 358, 97]
labels = ["USA MEN", "USA WOMEN", "CAN MEN", "CAN WOMEN", "NOR MEN", "NOR WOMEN"]
colors = ["blue", "blue", "red", "red", "Green", "Green"]
explode = (0.01,0.01,0.01,0.01,0.01,0.01)

plt.title("Top Country Medals Won by Gender", pad="20")

plt.pie(values, labels=labels, colors=colors, explode=explode)
plt.show()