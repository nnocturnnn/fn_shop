import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']

#Open database
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

#Create table
cur.execute('''CREATE TABLE users 
		(userId SERIAL PRIMARY KEY, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT
		)''')

cur.execute('''CREATE TABLE categories
		(categoryId SERIAL PRIMARY KEY,
		name TEXT
		)''')

cur.execute('''CREATE TABLE products
		(productId SERIAL PRIMARY KEY,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT,
		stock INTEGER,
		categoryId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
		)''')

cur.execute('''CREATE TABLE kart
		(userId INTEGER,
		productId INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')

conn.commit()
cur.close()
conn.close()

