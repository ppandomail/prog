import sqlite3

con = sqlite3.connect("tutorial2.db") # si no existe, la crea
cur = con.cursor()
cur.execute("CREATE TABLE peliculas(titulo, año, recaudacion)")
cur.execute("""
    INSERT INTO peliculas VALUES
        ('Avatar', 2009, 2.92),
        ('Titanic', 1997, 2.26),
        ('Jurassic', 2015, 1.67),
        ('Rey León', 2019, 1.66)
        
""")
con.commit()
for row in cur.execute("SELECT año, titulo FROM peliculas ORDER BY año"):
    print(row)
cur.execute("DROP TABLE peliculas")
con.close()
