import numpy as np
import pandas as pd


df = pd.read_csv("Burgerista Data.csv", header=None)
df.columns = ["col1", "col2"]

col1_split = df['col1'].str.split(';', expand=True)
col1_split.columns = ['date_transaction', 'payment_reference', 'date', 'price_euro']
col2_split = df['col2'].str.split(';', expand=True)
col2_split.columns = ['price_cent', 'currency', 'date_transaction_exact']
df = pd.concat([col1_split, col2_split], axis=1)

reference_split = df['payment_reference'].str.split(' ', expand=True)
time = reference_split[reference_split.columns[[10]]]
time.columns = ['time']
df = pd.concat([df, time], axis=1)


df['price_euro'] = df['price_euro'].str.replace('-', '')
df['price'] = df['price_euro'] + '.' + df['price_cent']

df = df.drop(['price_euro', 'price_cent', 'date_transaction_exact', ], axis=1)

df = df.astype({'price': "float64"})
df['date_transaction'] = pd.to_datetime(df['date_transaction'], format='%d.%m.%Y')
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
df['time'] = pd.to_datetime(df['time'], format='%H:%M')


df.to_csv("cleaned_data.csv")
# df = df[df.columns[cols]]


