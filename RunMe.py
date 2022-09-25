#database init program
import sqlite3
con=sqlite3.connect("NumberBaseConverterLoggingGithub.db")
cur = con.cursor()
cur.execute("CREATE TABLE logging(logs))")
