import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as snb

#1. Load Dataset
df=pd.read_csv('SampleSuperstore.csv')
df.head() #First Few Rows

#2. Understanding Dataset
print("(Rows,Columns):",df.shape)
print("Column Names:",df.columns)
print("Data Types:",df.info())
print("Summary:",df.describe())

#3. Basic Understanding
print("Total Number of Orders:",len(df))
print("Total Number of Consumers:",df.groupby('City')['Segment'].count())

total_sales=df.groupby('City')['Sales'].sum()
print("\nSales By City:\n",total_sales)
print("\nWhich City has Highest Sales?:\n",total_sales.sort_values(ascending=False))
high_city=total_sales.idxmax()
print(f"{high_city} generates the highest revenue among all cities.")

#4. Sales Analysis
cat_sales=df.groupby('Category')['Sales'].sum()
print("\nCategory-Wise Sales (Top-Bottom):\n",cat_sales.sort_values(ascending=False))
high_cat=cat_sales.idxmax()
print(f"{high_cat} category has been most demanding")
subcat_sales=df.groupby('Sub-Category')['Sales'].sum()
print("\nSub-Category Wise Revenue:\n",subcat_sales.sort_values(ascending=False))
high_subcat=subcat_sales.idxmax()
print(f"{high_subcat} has highest revenue")

#5. Profit Analysis
totalreg_prof=df.groupby('Region')['Profit'].sum()
print("Region-Wise Profits:",totalreg_prof)
print(f"{totalreg_prof.idxmax()} region has the highest profit")
totalcat_prof=df.groupby('Category')['Profit'].sum()
print("Category-Wise Profits:",totalcat_prof)
print(f"{totalcat_prof.idxmax()} category has the highest profit")
loss=df[df['Profit']<0]
loss_prod=loss.groupby('Sub-Category')['Profit'].sum()
print("\nTop 5 Loss Making Products:\n",(loss_prod.sort_values(ascending=True)).head(5))
high_loss=((loss_prod.sort_values(ascending=True)).head(5)).idxmin()
print(f"{high_loss} is most Loss-Making product")

#5. Shipping Analysis
high_ship=df['Ship Mode'].value_counts()
print(high_ship)
print(f"{high_ship.idxmax()} is the most preferred ship class")
ship_prof=df.groupby('Ship Mode')['Profit'].sum()
print(ship_prof.sort_values(ascending=False))
slow_ship=(ship_prof['Standard Class']+ship_prof['Second Class'])
fast_ship=(ship_prof['First Class']+ship_prof['Same Day'])
print("\nDoes faster shipping reduce profit?:")
if(slow_ship>fast_ship):
    print("Yes")
else:
    print("No")
#6. Customer Analysis
print(df.groupby('Segment')['Quantity'].sum())
high_seg=df.groupby('Segment')['Quantity'].sum().idxmax()
print(f"{high_seg} segment buys the most")

#6. Discount Analysis
print(df.groupby('Region')['Discount'].mean())
print(f"{df.groupby('Region')['Discount'].mean().idxmax()} region has most discounts")
totalreg_disc=df.groupby('Region')['Discount'].mean()
print(totalreg_prof,totalreg_disc)
highreg_prof=totalreg_prof.idxmin()
highreg_disc=totalreg_disc.idxmax()
print("\nDoes higher discount reduce profit?:")
print(df[['Discount','Profit']].corr())