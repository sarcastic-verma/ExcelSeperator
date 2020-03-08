import pandas as pd


#this is for work
def Seperator(Column,columnData,pathToSave=""):
    Column = Column
    name = columnData
    path=pathToSave
    df = demo[demo[Column]==name]
   #df = df.iloc[:, 0:20] #uncomment this to view only a specific no of cols
    file = path+columnData + ".xlsx" #this will create a seperate file in the specified path
    writer = pd.ExcelWriter(file, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()


    #to read file
xlsx = pd.ExcelFile(r'/home/noobie/Desktop/Workspace/hello.xlsx')
demo_sheets = []
for sheet in xlsx.sheet_names:
    demo_sheets.append(xlsx.parse(sheet))
    demo = pd.concat(demo_sheets,sort=False)
Column = input("Enter the column to be searched ")
data = input("Enter the data to be seperated ")
path = input("Enter the path to create the new file with seperated data: ")
Seperator(Column,data,path)
