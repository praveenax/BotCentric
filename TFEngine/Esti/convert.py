import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']= '3'

data = pd.read_csv("example.csv")
print(data)

data = data.join(pd.get_dummies(data["category"]))
data = data.drop("category", axis=1)
print(data)