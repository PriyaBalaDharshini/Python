import numpy as np
import matplotlib.pyplot as plot
# Randam Data
# rand: randam float b/w 0 1
# randint Generate a random int
# Distributions:  Normal distribution, Uniform Dist, Binominal Distribution - Important
# print(np.random.rand())
# print(np.random.rand(4))

# print(np.random.randint(10)) #end vale is not included
# print(np.random.randint(30, 66, size=7)) # start, end, how many values needed

# print(np.random.normal(loc=10, scale=10, size=20)) #loc = mean scal = STD
# print(np.random.uniform(5, 10, 5))

# np.random.seed(50) #same randaom number usefull for testing and reproduceing
# print(np.random.rand())
# print(np.random.rand(4))

# A normal distribution plot

data = np.random.normal(loc=10, scale=10, size=20000)

plot.hist(data, bins=100, density=True, alpha=0.4, color="g")
plot.xlabel("Values")
plot.ylabel("Frequency")
plot.title("Normal Distribution with mean=100, std=50, size=20000")
plot.show()
