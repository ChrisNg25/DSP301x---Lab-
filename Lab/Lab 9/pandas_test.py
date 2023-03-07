import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/phamdinhkhanh/datasets/master/BostonHousing.csv", sep=",", header = 0, index_col = None)
df.head()