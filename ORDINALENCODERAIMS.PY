import pandas as pd
import numpy as np
data = {
    'Quality': ['Good', 'Average', 'Bad', 'Excellent', 'Good', 'Average'],
    'Fruits': ['Mango', 'Apple', 'Grapes', 'Banana', 'Cherry', 'Watermelon']
}
df = pd.DataFrame(data)
quality_mapping = {
    'Bad': 1,
    'Average': 2,
    'Good': 3,
    'Excellent': 4
}


encoded_quality = []
for qual in df['Quality']:
    if qual == 'Bad':
        encoded_quality.append(1)
    elif qual == 'Average':
        encoded_quality.append(2)
    elif qual == 'Good':
        encoded_quality.append(3)
    elif qual == 'Excellent':
        encoded_quality.append(4)
    else:
        encoded_quality.append(np.nan)


df['encoded_quality'] = encoded_quality


print(df)








    



