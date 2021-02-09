import psycopg2

conn = psycopg2.connect(
    "host=127.0.0.1 dbname=test1 user=etsh password=3894")

cursor = conn.cursor()

# Drop table if exists to avoid error
cursor.execute('DROP TABLE IF EXISTS table1')
# Content tuple content for table1
content = '''
  id INTEGER PRIMARY KEY,
  completed BOOLEAN NOT NULL DEFAULT False
'''
cursor.execute('CREATE TABLE table1 (' + content + ');')

cursor.execute('INSERT INTO table1 (id, completed) VALUES (%s,%s);', (1, True))
cursor.execute(
    'INSERT INTO table1 (id, completed) VALUES (%s,%s);', (2, False))
cursor.execute('INSERT INTO table1 (id, completed) VALUES (%s,%s);', (3, True))
cursor.execute('INSERT INTO table1 (id, completed) VALUES (%s,%s);', (4, True))

cursor.execute('SELECT * FROM table1 WHERE completed = True')
fetchedData = cursor.fetchall()

conn.commit()
print(fetchedData)

cursor.close()
conn.close()
