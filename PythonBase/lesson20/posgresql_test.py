import psycopg2

# connect to db
connect = psycopg2.connect(host='localhost', database='testBase', user='angelina', password='2277')
try:
    with connect:
        with connect.cursor() as cursor:
            # execute query
            cursor.executemany('INSERT INTO user_account VALUES (%s, %s)', [(8, 'Mark'), (9, 'Den')])
            cursor.execute('SELECT * FROM user_account')
            # connect.commit()
            rows = cursor.fetchall()

            for row in rows:
                print(row)
finally:
    connect.close()
