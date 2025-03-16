import sqlite3

db_name = "Carvana_data"

connection = sqlite3.connect(db_name)

print(f"Connected to database: {db_name}")

cursor = connection.cursor()

# filters = {
#    'suv': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiU3V2Il19fQ',
#    'sedan': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiU2VkYW4iXX19',
#    'truck': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiUGlja3VwIl19fQ',
#    'coupe': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiQ291cGUiXX19',
#    'minivan': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiTWluaVZhbiJdfX0',
#    'convertible': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiQ29udmVydGlibGUiXX19',
#    'wagon': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiV2Fnb24iXX19',
#    'hatchback': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiSGF0Y2hiYWNrIl19fQ',
#    'electric': 'eyJmaWx0ZXJzIjp7ImZ1ZWxUeXBlcyI6WyJFbGVjdHJpYyJdfX0',
#    'pluginhybrid': 'eyJmaWx0ZXJzIjp7ImZ1ZWxUeXBlcyI6WyJQbHVnLUluIEh5YnJpZCJdfX0',
#    'hybrid': 'eyJmaWx0ZXJzIjp7ImZ1ZWxUeXBlcyI6WyJIeWJyaWQiXX19'
#}

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Categories (
#     category_id TEXT PRIMARY KEY,
#     category_name TEXT NOT NULL
# );
# """)
# print("Table 'Categories' created successfully.")


#for category_id,category_name,  in filters.items():
#    cursor.execute("""
#    INSERT OR REPLACE INTO Categories (category_id,category_name)
#    VALUES (?, ?);
#    """, (category_id, category_name))

# print("Data inserted into 'Categories' table successfully.")

#cursor.execute("SELECT * FROM Categories;")
#rows = cursor.fetchall()

# Print the results
#for row in rows:
#    print(row)
    
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Cars (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     link TEXT NOT NULL,
#     category_id TEXT NOT NULL,
#     FOREIGN KEY (category_id) REFERENCES Categories(id)
# );
# """)    

cursor.execute("Select * from Cars")
cars = cursor.fetchall()
for car in cars:
    print(car)

connection.close()

