#This program is initializing the database only.
#If I am being run before and the database's file isn't being deleted, I needn't run again or error may come up.
#to check if the database file is still on your local, you can run the converter's code. If it says TABLE not exist, run me now.
#database init program
import sqlite3
con=sqlite3.connect("NumberBaseConverterLoggingGithub.db")
cur = con.cursor()
cur.execute("CREATE TABLE logging(logs))")
