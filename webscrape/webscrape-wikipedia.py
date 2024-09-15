import pandas as pd
import ssl
import numpy as np

ssl._create_default_https_context = ssl._create_unverified_context


tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_best-selling_video_games')

print(len(tables))

table = tables[1]
print(table['Sales'])

listsales = [table['Sales'][x] for x in range(len(table))]

table['Sales'].to_csv('re.csv')

print(sum(listsales)/(len(listsales)))
print(np.average(listsales))