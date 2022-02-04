from re import S
import pandas as pd

df=pd.read_csv('pandas\GiftItems.csv')

# for index, row in df.iterrows():#traverses the rows
#     print(row['Name'] if row['Legendary']==True else print(f"{index} is not legendary"))

#locates specific row
# print(df.loc[df['Name']=="Pikachu"])

#describes the dataframes, mean, max, min, standard deviation etc
# print(df.describe())

#sorts rows
# print(df.sort_values("HP",ascending=False))

#advances sorting
# print(df.sort_values(['Type 1','HP'],ascending=False))
#print(df.sort_values(['Type 1','HP'],ascending=[1,0])) #"Type 1" ascending and HP descending
# print(df.sort_values(['Name','Legendary'],ascending=[0,1])) #Name descending, legendary ascening



#adding cols to the data
# df['Total']=df['HP']+df['Attack']
# print(df.head(2))

#adding the same col, the smart way
# df['Total']=df.iloc[:,4:10].sum(axis=1)
# print(df.head(4))


#removing a col
# df['kuchh bhi']=df['HP']+df['Attack']
# df=df.drop(columns=['Total'])
print(df.head())


#get the cols as a list
# print(list(df.columns.values))


#rearranging cols, getting total after "Type 2" col
# df['Total']=df.iloc[:,4:10].sum(axis=1)
# cols=list(df.columns)
# df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
# print(df.head(3))



#saving a modified csv file
# df['Total']=df.iloc[:,4:10].sum(axis=1)
# cols=list(df.columns)
# df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
# print(df.head(3))
# df.to_csv('modified.csv')



# # saving a modified csv file,without the index
# df['Total']=df.iloc[:,4:10].sum(axis=1)
# cols=list(df.columns)
# df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
# print(df.head(3))
# df.to_csv('pandas\modified.csv',index=False)



# saving a modified excel file,without the index
df['Total']=df.iloc[:,4:10].sum(axis=1)
cols=list(df.columns)
df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
print(df.head(3))
df.to_excel('pandas\modified.xlsx',index=False)



# saving modificaions as txt file
# df['Total']=df.iloc[:,4:10].sum(axis=1)
# cols=list(df.columns)
# df=df[cols[0:4]+[cols[-1]]+cols[4:12]]
# print(df.head(3))
# df.to_csv('pandas\modified.txt',index=False,sep="\t")



#advanced stuff
# advanced search
# print(df.loc[(df['Type 1']=="Fire") | (df['HP']<10)])

#saving filtered data
# new_frames=df.loc[(df['Type 1']=="Fire") & (df['HP']<50)]
# new_frames.to_csv('filtered1.csv') #this also saves the random indexes, which makes working with this file difficult



#saving filtered data without the random indexes, but saves the old indices
# new_frames=df.loc[(df['Type 1']=="Fire") & (df['HP']<50)]
# new_frames=new_frames.reset_index()  #this resets the indexes
# new_frames.to_csv('pandas\modifedwithrightindexes.csv')




#saving filtered data without the random indexes and drops the old indices
# new_frames=df.loc[(df['Type 1']=="Fire") & (df['HP']<50)]
# new_frames=new_frames.reset_index(drop=True)  #this resets the indexes
# new_frames.to_csv('pandas\modifedwithrightindexes.csv')



#getting name sthat contain Mega
# print(df.loc[df['Name'].str.contains("Mega")])


#getting names that dont contain Mega
# print(df.loc[df['Name'].str.contains("Mega")])



# advanced filtering with contains
# print(df.loc[df['Type 1'].str.contains("Fire|Grass")])#finds pokemon with type1 Grass or Fire
# import re #regular expression module
# print(df.loc[df['Type 1'].str.contains("fire|grass",flags=re.I)])#ignores casing
#matching using regex
# print(df.loc[df['Name'].str.contains('rai[a-z]*',flags=re.I)])




#changing values in the column, changing Fire type to Flame
# df.loc[df['Type 1']=="Fire",'Type 1']="Flame" #changing fire to flame
# df.loc[df['Type 1']=="Flame","Type 1"]="Fire" #fixing the mess
# print(df.head(50))



# changing multiple cols conditionally
# df.loc[df['HP']>50,['Generation','Legendary']]=['Test generation','Test legendary']
# print(df.loc[df['HP']>50])



#statistics with groupBy
# data=df.groupby(['Type 1']).mean().sort_values('Attack',ascending=False)#every Type's mean values
# print(data)



# data=df.groupby(['Type 1']).sum().sort_values('Attack',ascending=False)#every Type's mean values
# print(data)