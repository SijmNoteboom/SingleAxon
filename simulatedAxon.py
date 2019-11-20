import random as rand
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(columns=['stimulus'])
for i in range(100):
    df = df.append({'stimulus': rand.uniform(1, 3)}, ignore_index=True)
print(df)

response = np.random.randint(2, size=100) * 2 + np.random.normal(0, .1, 100)

df['response'] = response

plt.scatter(df['stimulus'], df['response'])
plt.show()