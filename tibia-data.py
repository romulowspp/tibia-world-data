import urllib.request
import json
import numpy
import matplotlib.pyplot as plt

import pandas

plt.close('all')

data = pandas.read_json('https://api.tibiadata.com/v2/world/belobra.json')

df = pandas.DataFrame(data['world']['players_online'], columns=['level', 'vocation']).sort_index(axis = 0)
df2 = df.pivot_table(values='level', index=df.index, columns='vocation')

range_values = numpy.arange(1, 750, 50)


ts = df2.groupby(pandas.cut(df['level'], range_values)).count()
print(ts)
ts.plot.bar()
plt.show()