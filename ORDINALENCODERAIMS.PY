#Ordinal encoder 
import pandas as pd
import numpy as np
data = {
 'Quality': ['Good' , 'Average', 'Bad','Excellent','Good','Average'],
 'Fruits' : ['Mango', 'Apple','Grapes','Banana','Cherry','Watermelon']
}
df1 = pd.DataFrame(data)

quality_mapping= {
    'Bad':1,
    'Average':2,
    'Good': 3,
    'Excellent':4
}
df1['encoded_quality'] = df1['Quality'].map(quality_mapping)

print(df1)
    



