import matplotlib.pyplot as plt

#years = [1900, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
#pops = [1.6, 2.5, 2.6, 3.0, 3.3, 3.6, 4.2, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

#plt.plot(years, pops, color=(0/255, 100/255, 100/255), linewidth=3.0)

#plt.ylabel("World Population")
#plt.xlabel("Population Growth")

#plt.title("World Population Growth", pad="20")

#plt.show()

#import matplotlib.pyplot as plt

# 1924 8 medals, 1928 11 medals, 1932 19 medals, 1936 12 medals, 1948 19 medals
# 1952 16 medals, 1956 19 medals, 1960 20 medals, 1964 7 medals, 1968 19 medals 
# 1972 1 medals, 1976 3 medals, 1980 2 medals, 1984 4 medals, 1988 6 medals
# 1992 36 medals, 1994 39 medals, 1998 48 medals, 2002 74 medals, 2006 67 medals
# 2010 90 medals, 2014 89 medals


years = [1924, 1928, 1932, 1936, 1940, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
pops = [8, 11, 19, 12, 15, 19, 16, 19, 20, 7, 19, 1, 3, 2, 4, 6, 36, 39, 48, 74, 67, 90, 89]

plt.plot(years, pops, color=(255/255, 0/255, 0/255), linewidth=3.0)

plt.ylabel("Won Medals")
plt.xlabel("Years")

plt.title("Medals Won by Year in Canada", pad="20")

plt.show()