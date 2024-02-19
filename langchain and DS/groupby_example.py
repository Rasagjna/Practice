import pandas as pd
df = pd.read_csv('weather_data.csv')
g= df.groupby('city')
for city, city_df in g:
    print(city)
    print(city_df)

g.get_group('mumbai')
#split, apply, combine
g.max()

g. mean()
g.describe()
g.plot

############################################

import pandas as pd
india_weather = pd.DataFrame(
    {
    "city" : ["mumbai", "delhi", "banglore"],
    "temperature" : [32,45,30],
    "humidity" : [80,60,78]
}
)

us_weather = pd.DataFrame({
    "city" : ["newyork","chicago","orlando"],
    "temperature" : [21,14,35],
    "humidity" : [68,65,75]
})
#ignores index in original dataframe, provides continuous index. Example: instead of  (0,1,2 ; 0,1,2) -> (0,1,2,3,4,5)
df=pd.concat([india_weather,us_weather],ignore_index=True)

df = pd.concat([india_weather,us_weather], keys=["india","us"])
df.loc["india"]

# axis argument, 
s = pd.Series(["Humid","Dry","Rain"], name="event")

# pd.merge -> merging datasets -> generates intersection like inner join
pd.merge(df1,df2,on="city",how="inner") #how="outer","left"

#indicator = True

# pivot allows you to transform or reshape data
df.pivot(index = "date", columns="city",values="humidity")

#pivot table is used to summarize and aggregate data inside dataframe


df.pivot_table(index = "city", columns="date",aggfunc="sum")
#aggfunc = count,mean
df.pivot_table(index= "city", columns="date", margins=True)
