print("https://stackoverflow.com/a/57406537")

import pandas as pd
import numpy as np
import pandas as pd

press_df = [['h',1649051432.9336905],
['o',1649051432.9806945],
['w',1649051433.0856972],
['Key.space',1649051433.180727],
['a',1649051433.2856908],
['r',1649051433.396689],
['e',1649051433.4846911],
['Key.space',1649051433.580691],
['y',1649051433.6846907],
['o',1649051433.7736928],
['u',1649051433.844697]]

release_df = [['h',1649051433.0536935],
['o',1649051433.1416924],
['w',1649051433.197692],
['Key.space',1649051433.3246918],
['a',1649051433.460688],
['r',1649051433.5576925],
['e',1649051433.629695],
['Key.space',1649051433.7176995],
['y',1649051433.797692],
['o',1649051433.900688],
['u',1649051433.9896967]]

press_df = pd.DataFrame(press_df, columns = ['keys', 'press_time'])
release_df = pd.DataFrame(release_df, columns = ['keys', 'release_time'])

press_df.reset_index(inplace=True, drop=True)
release_df.reset_index(inplace=True, drop=True)

press_df['g'] = press_df.groupby(['keys']).cumcount()
release_df['g'] = release_df.groupby(['keys']).cumcount()
print(press_df)
print(release_df)

merge_df = pd.merge(press_df, release_df, on=['keys', 'g'] , how='inner')
merge_df = merge_df.drop(columns=["g"])

# merge_df = pd.merge(press_df.drop_duplicates(), release_df.drop_duplicates(), on=['keys'], how='inner')
# print(df)
# merge_df = press_df.merge(release_df, how="cross")
# merge_df = pd.concat([press_df, release_df], join="inner", axis=1, keys="keys")

print(merge_df)
