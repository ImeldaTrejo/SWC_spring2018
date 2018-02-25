
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

my_file=pd.read_table("gapminder.txt")

Canada=my_file.loc[my_file['country']=="Canada",:]
Canada.plot.line(x="year",y="lifeExp", label="Life Expenctancy", figsize=(8,6))
plt.suptitle("Life Expectancy in Canada over the yers", fontsize=20)
plt.xlabel("Year",fontsize=16)
plt.savefig("PlotLifeExp.png")

