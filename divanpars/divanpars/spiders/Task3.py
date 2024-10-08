import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла, пропуская первую строку
df = pd.read_csv('price.csv')

df['price'] = df['price'].str.replace(' ', '')
print(df.head())

# scrapy crawl divannewpars