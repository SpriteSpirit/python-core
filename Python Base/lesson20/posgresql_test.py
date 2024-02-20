import psycopg2

# connect to db
connect = psycopg2.connect(
    host='localhost',
    database='testBase',
    user='angelina',
    password='2277'
)

# create cursor
cursor = connect.cursor()

# execute query
cursor.execute('INSERT INTO user_account VALUES (%s, %s)', (5, 'Tedd'))
cursor.execute('SELECT * FROM user_account')

connect.commit()

rows = cursor.fetchall()

for row in rows:
    print(row)

# close cursor and connection
cursor.close()
connect.close()
