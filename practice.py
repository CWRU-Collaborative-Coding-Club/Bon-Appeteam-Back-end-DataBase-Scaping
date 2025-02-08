import MySQLdb

db = MySQLdb.connect(
    host="db4free.net",      
    user="bklee46",  
    passwd="heratree",
    db="bonnapp",    
    port=3306        
)

# Create a cursor object using a cursor() method
cursor = db.cursor()

#add practice query here
query = """

"""


cursor.execute(query)


# Execute an SQL query using execute() method
cursor.execute("SHOW TABLES")

# Fetch all results using fetchall() method
tables = cursor.fetchall()

# Print the tables
for table in tables:
    print(table)

# Close the connection
db.close()