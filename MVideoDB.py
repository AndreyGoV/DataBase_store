import sqlite3
import pandas as pd


sql = sqlite3.connect('Electronics store.db')

# Создаём таблицу с категориями товаров
category = ['Смартфоны', 'Ноутбуки', 'Смарт-часы']
category_df = pd.DataFrame({'category': category})
category_df

category_df.to_sql('category', sql, index_label='id', if_exists='replace') # Сохраним в базу
pd.read_sql('SELECT * FROM category', sql) # Проверим, что сохранилось правильно

# Создаём таблицу с брендами
brand = ['Apple', 'Samsung', 'Huawei', 'Xiaomi']
brand_df = pd.DataFrame({'brand': brand})
brand_df

brand_df.to_sql('brand', sql, index_label='id', if_exists='replace') # Сохраним в базу
pd.read_sql('SELECT * FROM brand', sql) # Проверим, что сохранилось правильно

model = ['iPhone 13', 'iPhone 14', 'Galaxy S21', 'Galaxy A13', 'Readmi 10', 'Mi 11T',
         'Mate 50', 'Nova 10', 'MacBook Air 13', 'MacBook Pro 13', 'MateBook D15',
         'MateBook D14', 'RedmiBook 15', 'FIT 2 Active', 'Watch Fit New',
         'Galaxy Watch 5', 'Apple Watch Ultra']
category_id = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2]
brand_id = [0, 0, 1, 1, 2, 2, 3, 3, 0, 0, 2, 2, 3, 2, 2, 1, 0]
price = [75000, 109990, 42999, 12000, 15990, 29999, 69999, 39990,
        80999, 107999, 58999, 46999, 49999, 7499, 5299, 16999, 79990]
amount = [98, 505, 169, 45, 90, 91, 56, 43, 10, 45, 50, 9, 5, 17, 54, 70, 143]

catalog_df = pd.DataFrame({
    'model': model,
    'brand_id': brand_id,
    'category_id': category_id,
    'price': price,
    'amount': amount
})

catalog_df

catalog_df.to_sql('catalog', sql, index_label='id', if_exists='replace')
pd.read_sql('SELECT * FROM catalog', sql)


# Объединение таблиц
pd.read_sql(
    '''
    SELECT ctlg.model as model,
    b.brand as brand,
    c.category as category,
    ctlg.price,
    ctlg.amount
    FROM catalog AS ctlg
    LEFT JOIN brand AS b ON b.id = ctlg.brand_id
    LEFT JOIN category AS c ON c.id = ctlg.category_id
    ''',
    sql)s
