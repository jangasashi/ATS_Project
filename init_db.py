# init_db.py
import database

database.create_users_table()
database.create_match_log_table()
print("Tables created.")