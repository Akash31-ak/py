#pandas-
#installl pandas = py -m pip install pandas
import pandas as pd

# s = pd.Series([10,20,30],index=['a','b','c'])
# print(s)
# print(s['b'])
# print(s.values)

data = {
    "Name":["Alice","Bob","Charlie","David"],
    "Age" :[19,20,22,24],
    "Score":[55,64,34,87]
}
df = pd.DataFrame(data,index=['a','b','c','d'])
print(df)
#Row access using iloc[]-> access row by integer position (index)
print(df.iloc[1])
#Row access using loc[]-> access row by integer position (index)
print(df.loc['c'])
#masking in dataframe
print(df[df["Score"]>55])
df["Grade"]=["B","C","A","A+"]
print(df)
df.drop("Age",axis =1)#axis 1 denotes the row("Age" is the row name) to delit permenant we use (,inplace=true)
print(df)
df.rename(columns={"Score":"Marks"},inplace=True)
print(df)
import numpy as np
df1 = pd.DataFrame({
    "Food":["Rice","Dal","Roti",None],
    "Price":[20,40,50,np.nan]
})
print(df1.isnull())
df1.fillna("Unknown")#replace the null values if use (,inplace=True)it will replace it
print(df1)
df1.dropna(inplace=True)
print(df1)
#aggregate function 
print(df.describe())
print(df.mean(numeric_only=True))
print(df.groupby("Grade")["Marks"].mean())

df2 = pd.read_csv("currency.csv")
print(df2.head())#first 5 rows
print(df2.head(10))
print(df2.tail())#last 5 rows

df.to_csv("student.csv",index=False)
#for read any excel file
#df = pd.read_excel("data.xlsx")
#df.to_excel("output.xlsx")

print(df[0:2])#slicing
df.set_index("Name",inplace=True)
print(df)
df.reset_index(inplace=True)
print(df)

s = pd.Series([10,20,30],index=['a','b','c'])
print(s)
print(s['b'])
print(s.values)

s1 = pd.Series({'x': 5, 'y': 10, 'z':15})
print(s.index)
print(s1.index)
print(s.dtype)
print(s.size)
print(s.shape)
print(s1[['x','z']])
s1['x']=20#update the value
print(s1)
s1['w']=25#add new items in the series 
print(s1)
s1.drop('y',inplace=True)
print(s1)

x = pd.Series([10,20,30])
print(x[x>20])
print(x*10)
print(x+2)
print(x**2)

y = pd.Series([10,None,30,np.nan,40,70])
print(y.isnull())
y.dropna(inplace=True)
print(y)

z = pd.Series([10,20,30,40,50])
print(z.sum())
print(z.mean())
print(z.min(),z.max())
print(z.std())
print(z.describe())


names = pd.Series(["Alice","Bob","Charlie","David"])
print(names.str.upper())
print(names.str.capitalize())
print(names.str.contains("a"))#case sensitive

x1 = pd.Series([30,10,40,20], index=['d','b','a','c'])
print(x1.sort_values()) #sort by values
print(x1.sort_index())  # sort by index
print(x1.rank())        #rank based on values

y1 = pd.Series([5,15,25], index=['b','c','d'])
y2 = pd.Series([10,20,30], index=['a','b','c'])
print(y1+y2)

#matplotlib
#py -m pip install matplotlib
import matplotlib.pyplot as plt
#basic plot
x = [1,2,3,4,5]
y = [10,11,18,13,14]
#plt.plot(x,y,color="green",marker='^',linestyle='--',linewidth=2)#marker can be 's'=square,'o'=circle,'^'=triangle
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("My first graph")
# plt.grid(True)
#plt.show()
y1 = [1,4,9,16,25]
y2 = [25,16,9,4,1]
# plt.plot(x,y1,label="X-Y1graph")
# plt.plot(x,y2,label="X-Y2graph")
# plt.legend()
#plt.show()
#3bargraph
categories = ['A','B','C','D']
values = [10,24,36,18]

# plt.bar(categories, values , color='skyblue')
# plt.title("Bar chart Example")
# plt.show()
#scatter plot
a = [5,7,27,7,2,3,2,9]
b = [99,86,87,88,100,86,103,87]
# plt.scatter(a,b,color='purple')
# plt.title("Scatter chart Example")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
#Histogram
# data = np.random.randn(1000)
# plt.hist(data, bins=30, color='teal', edgecolor='black')
# plt.title("Histogram of Random Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
sizes = [30,40,30,15]
labels = ['Python','Java','c++','Javascript']
# plt.pie(sizes, labels=labels, autopct='%1.1f%%',startangle=90)
# plt.title("Programming language Usage")
# plt.axis('equal')
x = [1,2,3,4,5]
y = [5,1,8,3,4]
plt.subplot(1,2,1)#1r,2c,1p
plt.plot(x,y)
plt.subplot(1,2,2)#1r,2c,2p
plt.bar(x,y)
plt.tight_layout()
plt.savefig("plot1.png", dpi=300)
plt.show()



















