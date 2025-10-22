#One Hot Encoder
import pandas as pd
import numpy as np

data = {
    'colors': ['red', 'green', 'blue','red','green']
}
df1 = pd.DataFrame(data)

rainbow=df1['colors'].unique()

for colour in rainbow:
    df1[colour]  =[ 1 if x==colour else 0 for x in df1['colors'] ] 
    print(df1)  
