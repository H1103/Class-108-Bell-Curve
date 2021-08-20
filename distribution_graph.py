# we use plotly.figure_factory using scipy package
# We use distplot() to draw the distributoiin graph for the data 
# It takes two arguements that is the data and the label for the data
import random
import plotly.express as px 
import csv
import plotly.figure_factory as ff 

dice_result = []
count = []

for i in range(0,101):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)
    
fig = ff.create_distplot([dice_result],["Result"])
fig.show()

print(count)
print(dice1,dice2)