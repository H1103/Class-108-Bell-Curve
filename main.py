import random
import plotly.express as px 
import csv

dice_result = []
count = []

for i in range(0,101):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)
    
fig = px.bar(x = dice_result, y = count)
fig.show()

print(count)
print(dice1,dice2)