import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

missing_values = ["n/a", "NAN", "na", " "]
df1 = pd.read_csv('train.csv', na_values=missing_values, header=None)


# print(df1)
# print(df1.shape)

# a = df1.isnull()

# print(a)
# df_zero = df1.fillna(0)
# print(df_zero)


imp = SimpleImputer(missing_values=np.nan, strategy='mean')
print(imp)
imp.fit(df1)
df_mean = imp.transform(df1)
print(df_mean)