import pandas as pd
#dataframe object
df = pd.read_csv("nyc_weather.csv")
# print(df)
df["Temperature"].max()
print(df["EST"][df["Events"] == "Rain"])
df["WindSpeedMPH"].mean()
# the process of cleaning data is called data munging 
df.fillna(0,inplace = True) # fill NA with 0

#dataframe is a main object in pandas. It is used to represent data with rows and
#columns (tabular or excel spreadsheet like data)

rows, columns = df.shape
print(rows)
print(columns)
df.head() # first 5 rows
df.tail() # last 5 rows

df[2:5] # rows two to five

df[['event','day','temperature']]
df['temperature'].max()

df.describe()

df[df.temperature >=32]
df[['day','temperature']][df.temperature == df['temperature'].max()]

df.set_index('day',inplace = True)
# modifies the original dataframe, sets date as index

df.loc['1/3/2017']
df.reset_index(inplace=True)
df.set_index('event',inplace=True)

#read_csv
#read_excel
#pd.DataFrame() -> convert dictionary to dataframe
#pd.DataFrame(weather_data,columns = ["day","temperature","windspeed","event"]) -> convert tuple to dataframe

#when you have extra header, you can use skip header to skip no of rows

df = pd.read_csv("stock_data.csv",header = 1)
#or
df = pd.read_csv("stock_data.csv", skip_rows = 1)

# when there is no header, header = none
df = pd.read_csv("stock_data.csv", header = None,names= ["ticket","eps","revenue"])
# only to read specific rows , we can use nrows="no of rows you want to read"

# replace n.a and not available to NaN
df = pd.read_csv("stock_data.csv", na_values = ["not available","n.a."])
df = pd.read_csv("stock_data.csv",
                 na_values = {
                     'eps' : ["not available","n.a."],
                     "revenue" : ["not available", "n.a.",-1],
                     "people" : ["not available","n.a."]
                 }
                 )


df.to_csv("new.csv",columns=['temperature'], header = False)

def convert_people_cell(cell):
    if cell == 'n.a.':
        return 'sam walton'
    return cell
df = pd.read_excel("stock_data.xlsx", "Sheet1",converters={
    "people" : convert_people_cell
})

df.to_excel("new.xlsx", sheet_name = "stocks",startrow=1,startcol=2,index = False)

