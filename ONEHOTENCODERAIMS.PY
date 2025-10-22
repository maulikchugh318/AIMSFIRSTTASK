#One Hot Encoder
import pandas as pd
import numpy as np

data = {
    'color': ['red', 'green', 'blue','red','green']
}
df1 = pd.DataFrame(data)

rainbow=df1['color'].unique()

for colour in rainbow:
    df1[colour]  =[ 1 if x==colour else 0 for x in df1['color'] ] 
    print(df1)
