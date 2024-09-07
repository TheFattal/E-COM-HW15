
import sqlite3

conn = sqlite3.connect('FirstDbSQL.db')  # connection to the db
conn.row_factory = sqlite3.Row  # in order to use column name
cursor = conn.cursor()  # component to send queries

# SELECT
# Define the SQL query
query = '''
SELECT * from song_details;
'''
cursor.execute(query)  # send query
result = cursor.fetchall()  # gets a list of generators
list_results = [tuple(row) for row in result]  # generate result
for row in list_results:
    print(row)

# convert tuple to list
list_data = [list(tup) for tup in list_results]
print(list_data)

# UPDATE
# update_query = '''
#     UPDATE song_details
#     SET song_length_seconds = 180
#     WHERE year = 2018;
# '''
# cursor.execute(update_query)
# cursor.connection.commit()  # saves the data into the file -- write changes

conn.close()
