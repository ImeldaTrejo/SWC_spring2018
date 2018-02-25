
# coding: utf-8

# #Welcome all

# #Welcome all

# # Welcome all

# In[2]:


3+5


# In[3]:


print{Hello world}


# In[4]:


print{"Hello world"}


# In[5]:


print("Hello world")


# In[6]:


import math

sin(0)

sqrt(4)


# In[9]:


help(math)


# In[10]:


e


# In[12]:


math.sqrt(4)



# In[13]:


a=5


# In[14]:


print(a)


# In[15]:


dna="ATG"


# In[17]:


print(dna)


# In[18]:


mass = 47.5


# In[19]:


height = 24.5


# In[20]:


age = 122


# In[21]:


mass = mass * 2.3


# In[22]:


print(mass)


# In[23]:


age = age - 20


# In[24]:


print(age)


# In[25]:


height = height + 20    


# In[26]:


print(height)


# In[27]:


who


# In[28]:


del(a)


# In[29]:


who


# In[33]:


reset


# In[34]:


who


# In[35]:


print(dna)


# In[36]:


import math


# In[37]:


help(math)


# In[42]:


a=5.7


# In[39]:


print(a)


# In[40]:


dna="ATG"


# In[41]:


type(dna)


# In[43]:


type(a)


# In[44]:


b=4.3


# In[45]:


a+b


# In[47]:


int()=


# In[48]:


list=["Afghanistan","Asia",4,5,1987,6.2]


# In[49]:


print(list)


# In[52]:


list[1]


# # list is an ordered sequense of objects.
# # Index star from zero
# # List are mutable

# In[53]:


list[2:5]


# In[54]:


list[3]=187.55


# In[55]:


print(list)


# In[64]:


tuple=("Afghanistan", "Asia", 4, 187.55, 1987, 6.2)


# In[65]:


print(tuple)


# In[66]:


#tuple are ordered sequences of objects
#tuple are indexed and indexinf start from 0


# In[67]:


tuple[0]


# In[76]:


dict={1:"a",2:"b",'dna':"ATG"}


# In[77]:


dict[dna]


# In[78]:


print(dict)


# In[71]:


my_Order={'menuItems':["Chicken", "Soup"], 'menuType':["Solid", "Liquid"], 'menuCost':[4.99,2.99]}


# In[72]:


print(my_Order)


# In[79]:


import pandas as pd


# In[80]:


My_Order=pd.DataFrame(data=my_Order)


# In[81]:


print(My_Order)


# In[82]:


my_file=pd.read_table("gapminder.txt")


# In[83]:


pd.DataFrame(data=my_file)


# In[92]:


print(my_file.iloc[0,0])


# In[93]:


print(my_file.iloc[0:2,0:4])


# In[95]:


print(my_file.iloc[[0,1],[1,2]])


# In[99]:


my_file.loc[:,['year']]


# In[102]:


my_file.loc[1:5,['year','continent']]


# In[105]:


my_file.loc[my_file['country']=="Afghanistan"]


# In[108]:


ls=my_file['country']=="Afghanistan"


# In[109]:


print(ls)


# In[110]:


import matplotlib.pyplot as plt


# In[113]:


Canada=my_file.loc[my_file['country']=="Canada",:]


# In[114]:


print(Canada)


# In[122]:


Canada.plot.line(x="year",y="lifeExp", label="Life Expenctancy", figsize=(8,6))
plt.suptitle("Life Expectancy in Canada over the yers", fontsize=20)
plt.xlabel("Year",fontsize=16)
plt.savefig("PlotLifeExp.png")

