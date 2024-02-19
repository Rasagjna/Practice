import pandas as pd
import numpy as np
df = pd.read_csv('weather_data.csv')
new_df = df.replace([-99999,-8000],np.NaN)
new_df = df.replace({
    "temperature" : -99999,
    "windspeed" : -99999,
    'event' :'0'
},np.NaN)

new_df = df.replace({
    -99999: np.NaN,
    'No Event' : 'Sunny'
})

new_df = df.replace('[A-Za-z]', '',regex = True)
df.replace({
    'temperature': '[A-Za-z]',
    'windspeed': '[A-Za-z]'
},'', regex = True)

# replace one list by another list
df.replace(['poor', 'average','good','exceptional'],[1,2,3,4])
