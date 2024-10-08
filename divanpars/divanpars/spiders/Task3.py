import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('price.csv')

# Удаление пробелов и преобразование цен в целые числа
df['price'] = df['price'].str.replace(' ', '').astype(int)

# Вычисление средней цены
average_price = df['price'].mean()
print(f'Средняя цена на диваны: {average_price}')

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Количество диванов')
plt.grid(axis='y', alpha=0.75)
plt.show()