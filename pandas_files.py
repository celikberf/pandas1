import pandas as pd
import sqlite3

# df = pd.read_csv('sample.csv')
# df = pd.read_json('sample.json')
# df = pd.read_excel('sample.xlsx')

connection  = sqlite3.connect('sample.db')
df = pd.read_sql_query("SELECT * FROM students")

print(df)