import sqlite3
def registered(qq_id,root=0):
    s = sqlite3.connect("..../DataBash/user.db")
    c = s.cursor()
    c.execute(f"")