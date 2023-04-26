# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |

# import pandas as pd 
# import numpy as np 
# import random
 
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})
# print(data)
 
# #==================================================#
# data['tmp'] = 1
# data.set_index([data.index, 'whoAmI'], inplace=True)
# data = data.unstack(level=-1, fill_value = 0).astype(int)
# data.columns = data.columns.droplevel()
# data.columns.name = None
# print(data)

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame(lst ,columns={'WhoAmI'})
data.head()

# One hot вид (не уверен, сам из похожей проги переделал):

data = pd.DataFrame(random.sample(['robot', 'human']*10, 10) ,columns={'WhoAmI'})
data.head()