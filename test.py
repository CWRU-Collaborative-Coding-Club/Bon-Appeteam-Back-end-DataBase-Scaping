import MySQLdb

db = MySQLdb.connect(
    host="db4free.net",      # Replace with your host (e.g., localhost or an IP)
    user="bklee46",  # Replace with your MySQL username
    passwd="heratree", # Replace with your MySQL password
    db="bonnapp",    # Replace with your database name
    port=3306         # Replace with your MySQL port (usually 3306)
)

# Create a cursor object using a cursor() method
cursor = db.cursor()

query = """
CREATE TABLE food_items (
    id INT PRIMARY KEY,
    label VARCHAR(255),
    description TEXT,
    station VARCHAR(255),
    special BOOLEAN,
    tier INT,
    price DECIMAL(10,2)
);

"""
second = """ 
CREATE TABLE nutrition (
    food_id INT,
    calories INT,
    serving_size FLOAT,
    serving_unit VARCHAR(50),
    total_fat FLOAT,
    saturated_fat FLOAT,
    trans_fat FLOAT,
    cholesterol INT,
    sodium INT,
    carbohydrates FLOAT,
    fiber FLOAT,
    sugars FLOAT,
    protein FLOAT,
    FOREIGN KEY (food_id) REFERENCES food_items(id) ON DELETE CASCADE
);


"""
third = """
CREATE TABLE food_categories (
    food_id INT,
    category VARCHAR(100),
    FOREIGN KEY (food_id) REFERENCES food_items(id) ON DELETE CASCADE
);

"""

cursor.execute(query)
cursor.execute(second)
cursor.execute(third)

# Execute an SQL query using execute() method
cursor.execute("SHOW TABLES")

# Fetch all results using fetchall() method
tables = cursor.fetchall()

# Print the tables
for table in tables:
    print(table)

# Close the connection
db.close()