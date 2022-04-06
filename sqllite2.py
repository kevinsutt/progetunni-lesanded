import sqlite3




ühendus = sqlite3.connect('personal.db')
c = ühendus.cursor()
c.execute("SELECT * FROM opetajad")

c.execute("INSERT INTO opetajad (eesnimi,perekonnanimi, aastaid_koolis, arv) VALUES ('Kätlin', 'Kask', 16, 50)")


c.close()

ühendus.commit()

ühendus.close()
