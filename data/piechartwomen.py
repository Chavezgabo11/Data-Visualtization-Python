import matplotlib.pyplot as plt 
# Canada value 239 women
# United States 242 women

values = [239, 242]
labels = ["Canada", "United States"]
colors = ["Red", "lightskyblue"]
explode = (0,0.1)

plt.title("Women Medals Won", pad="20")

plt.pie(values, labels=labels, colors=colors, explode=explode)
plt.show()