import random as rand
import numpy as np
import pandas as pd

df = pd.DataFrame(columns=['stimulus'])
for i in range(100):
    df = df.append({'stimulus': rand.uniform(1, 3)}, ignore_index=True)
print(df)

df = df.append(self, )

x = 3