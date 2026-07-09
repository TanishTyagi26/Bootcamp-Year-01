import pandas as pd
# data={
#     'Name':['John','Anni','Tanish','Ayush'],
#             'Age': [28,24,35,32],
#             'City' : ['New York','Paris','Korea','London']
# }
# df=pd.DataFrame(data)
# # print( df['Name'])
# df['Salary ' ]  =  [70000 ,  80000 ,  120000 ,  90000]
# # print(df.describe())
# df_sorted =df.sort_values(by='Age')
# # print(df_sorted)
# df_filtered  =  df[df['Age']  >  30][ ['Age']]
# # print( df_filtered )


# print( df. loc [1:3])
# print( df. iloc [1:3])
# # print( df. iloc [1:3])


import matplotlib.pyplot as plt
data= {
    'Month ': ['Jan','Feb','Mar','Apr'],
    'Sales':[2500,2700,3000,3200]

}

df=pd.DataFrames(data)
plt.plot(df['Month'],df['Sales'],marker='o')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()