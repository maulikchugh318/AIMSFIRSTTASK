#Mean imputation
import pandas as pd 
import numpy as np
data = {
    'age':[25,np.nan,30,22,np.nan,28],
    'salary':[40000,30000,45000,np.nan,50000,np.nan],
    'Profession': ['Engineer','Dietician',np.nan,'Architect','Doctor','Artist']
}

df1=pd.DataFrame(data)
for imputation in ['age','salary']:
    mean_value=df1[imputation].mean()
    df1[imputation].fillna(mean_value,inplace=True)

    df1['Profession'].fillna('Unknown', inplace=True)
    print(df1)

    
    
