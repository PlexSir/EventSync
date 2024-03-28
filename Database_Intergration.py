python

import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object for executing SQL queries
cursor = db.cursor()

# Create events table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        description TEXT,
        date DATE
    )
""")

# Function to create a new event
def create_event(event):
    sql = "INSERT INTO events (title, description, date) VALUES (%s, %s, %s)"
    values = (event['title'], event['description'], event['date'])
    cursor.execute(sql, values)
    db.commit()
    return cursor.lastrowid

# Function to retrieve all events
def get_events():
    cursor.execute("SELECT * FROM events")
    return cursor.fetchall()

# Function to retrieve a specific event by ID
def get_event(event_id):
    sql = "SELECT * FROM events WHERE id = %s"
    cursor.execute(sql, (event_id,))
    return cursor.fetchone()

# Function to update an existing event
def update_event(event_id, event):
    sql = "UPDATE events SET title = %s, description = %s, date = %s WHERE id = %s"
    values = (event['title'], event['description'], event['date'], event_id)
    cursor.execute(sql, values)
    db.commit()

# Function to delete an event
def delete_event(event_id):
    sql = "DELETE FROM events WHERE id = %s"
    cursor.execute(sql, (event_id,))
    db.commit()

# Usage examples
event1 = {
    'title': 'Event 1',
    'description': 'Event 1 description',
    'date': '2024-03-28'
}

event2 = {
    'title': 'Event 2',
    'description': 'Event 2 description',
    'date': '2024-03-29'
}

event_id1 = create_event(event1)
event_id2 = create_event(event2)

print("Events:")
print(get_events())

print("Event 1:")
print(get_event(event_id1))

print("Updating Event 1...")
updated_event1 = {
    'title': 'Updated Event 1',
    'description': 'Updated Event 1 description',
    'date': '2024-03-30'
}
update_event(event_id1, updated_event1)

print("Events after update:")
print(get_events())

print("Deleting Event 2...")
delete_event(event_id2)

print("Events after delete:")
print(get_events())

# Close the database connection
db.close()