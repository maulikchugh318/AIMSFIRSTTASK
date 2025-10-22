import pandas as pd 
import numpy as np
data = {
    'age':[25,np.nan,30,22,np.nan,28],
    'salary':[40000,30000,45000,np.nan,50000,np.nan],
    'city': ['Delhi','Bangalore',np.nan,'Kolkata','Bombay','Surat']
}

df1=pd.DataFrame(data)
for mean_imputation in ['age','salary']:
    mean_value=df1[mean_imputation].mean()
    df1[mean_imputation].fillna(mean_value,inplace=True)

    df1['city'].fillna('Unknown', inplace=True)
    print(df1)
