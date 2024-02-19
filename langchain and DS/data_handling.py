import pandas as pd
df = pd.read_csv("weather_data.csv",parse_dates = ["day"])
type(df.day[0]) #timestamp
df.set_index("day",inplace = True)
df.fillna(0)
new_df = df.fillna({
    "temperature" : 0,
    "windspeed" : 0,
    "event" :"no event"
})

# if you have na value, carryforward the previous days value using ffill
new_df = df.fillna(method = "ffill")

# bfill -> next days value

new_df = df.fillna(method = "ffill",axis="columns",limit = 1)


new_df = df.interpolate()

new_df = df.dropna(how="all")

# thresh = 1, if you have atleast one non na value, keep the row
new_df = df.dropna(thresh=1)

