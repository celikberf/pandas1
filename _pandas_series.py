import pandas as pd
import numpy as np

#data
numbers = [20,30,40,50]
letters = ['a','b','c','d']
scalar = 5
dict= {'a': 10, 'b': 20, 'c': 30, 'd': 40}
random_numbers = np.random.randint(10,100,6)

# pandas_series = pd.Series(numbers) # her birine index numarası atanır ve #dtype: int64
# pandas_series = pd.Series(letters) # her birine index numarası atanır ve #dtype: object
# pandas_series = pd.Series(scalar) # dtype: int64
# pandas_series = pd.Series(scalar,[0,1,2,3]) # verdiğimiz index kadar arttırılır.#dtype: int64
# pandas_series = pd.Series(numbers,['a','b','c','d']) # index numaralarını kendimiz verdik
# pandas_series = pd.Series(dict) # direkt pandas serisi. Indexleri key olarak verdik
# pandas_series = pd.Series(random_numbers)  # numpy'denn verdiğimiz  random sayılar pandas series'e eklenir
# result = pandas_series[0]
# pandas_series = pd.Series([20,30,40,50],['a','b','c','d'])
# result = pandas_series[0]
# result = pandas_series[-1]
# result = pandas_series[:2]
# result = pandas_series[-2:]
# result = pandas_series['a']
# result = pandas_series['d']
# result = pandas_series[['a','c']]
# result = pandas_series.ndim # 1 boyutlu
# result = pandas_series.dtype # int64
# result = pandas_series.shape # (4,) 4 elemanlı tek boyutlu bir liste
# result = pandas_series.sum() # elemanlarının value değerleri : 140
# result = pandas_series.max() # 50
# result = pandas_series.min() # 20
# result = pandas_series + pandas_series # toplar ve value değerleri 2 katına çkmş olur
# result = pandas_series + 50 # her değere + 50 ekler.
# result = np.sqrt(pandas_series) # karekökünü aldık
# result = pandas_series >= 50 # 50den büyük ifadeler true false
# result = pandas_series %2 == 0 # true false

# print(pandas_series)
# print(result)

opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

total = opel2018 + opel2019 

print(total)