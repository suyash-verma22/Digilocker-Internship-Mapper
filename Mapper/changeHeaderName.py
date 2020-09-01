import pandas as pd
file = pd.read_csv("student_details.csv")

print(file.head())

#change header name from [name --> s_name ,department --> s_department, birthday month --> s_birthday]
header_names = ['s_name','s_department','s_birthday']

file = pd.read_csv("student_details.csv",header=None,skiprows=1,names=header_names)
print(file)

#dropping columns
col = []
for cols in file.columns:
    col.append(cols)

print(col)
drp_col = ['s_birthday']
file.drop(drp_col,axis=1,inplace=True)
print(file)

#if you want s_department to be the first column
file = file[["s_department","s_name"]]
print(file)

#download new modified csv file
file.to_csv("output.csv",index=False)