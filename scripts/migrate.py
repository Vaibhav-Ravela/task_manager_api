import os
import psycopg2
import pymongo
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL Connection
pg_conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)
pg_cursor = pg_conn.cursor()

# MongoDB Connection
mongo_client = pymongo.MongoClient(os.getenv("MONGO_URI"))
mongo_db = mongo_client[os.getenv("MONGO_DB")]
mongo_tasks = mongo_db.tasks

pg_cursor.execute("SELECT id, title, description FROM tasks")  # Removed created_at
tasks = pg_cursor.fetchall()

for task in tasks:
    task_dict = {
        "_id": task[0],
        "title": task[1],
        "description": task[2],
        "status": False,  # Default to False if missing
    }
    mongo_tasks.insert_one(task_dict)


print("✅ Migration Completed!")

# Close connections
pg_cursor.close()
pg_conn.close()
mongo_client.close()