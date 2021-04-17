import matplotlib.pyplot as plt 
# Canada value 385 men
# United States 409 men

values = [385, 409]
labels = ["Canada", "United States"]
colors = ["Red", "lightskyblue"]
explode = (0,0.1)

plt.title("Men Medals Won", pad="20")

plt.pie(values, labels=labels, colors=colors, explode=explode)
plt.show()