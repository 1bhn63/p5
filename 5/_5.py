import pandas as pd

dataset = pd.read_csv('iris.csv')

print(dataset)

print(dataset.info())

print(dataset.shape)

print(dataset.columns)

print(dataset['Species'].unique())

sorted_dataset = dataset.sort_values('SepalLengthCm')

print(sorted_dataset)

dataset = dataset.drop(columns=['SepalWidthCm'])

dataset = dataset.dropna()

print(dataset)

mean_value = dataset['PetalLengthCm'].mean()
dataset['PetalLengthCm'].fillna(mean_value, inplace=True)

print(dataset)

dataset = dataset.drop_duplicates()

print(dataset)

print(dataset.info())

print(dataset.describe())

subset = dataset.loc[0:4, ['SepalLengthCm', 'PetalLengthCm']]

print(subset)

dataset.to_csv('new_dataset.csv', index=False)