# import matplotlib.pyplot as plt
# plt.boxplot([1,2,3,100])
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd
df=pd.DataFrame({'x':[1,2,3,100]})
df.boxplot(column='x')
plt.show()
