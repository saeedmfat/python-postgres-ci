import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Function to get a database connection
def get_db_connection():
    # These environment variables will be provided by GitHub Actions
    conn = psycopg2.connect(
        host=os.environ.get('POSTGRES_HOST', 'localhost'),
        database=os.environ.get('POSTGRES_DB', 'testdb'),
        user=os.environ.get('POSTGRES_USER', 'postgres'),
        password=os.environ.get('POSTGRES_PASSWORD', 'password'),
        port=os.environ.get('POSTGRES_PORT', '5432')
    )
    return conn

# Function to get all users (for our test)
def get_users():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users