import sqlite3
# teeme tabeli lahti
ühendus = sqlite3.connect('rockyou.db')
c = ühendus.cursor()
# küsimus
print("ROCKYOU.TXT PAROOLI KONTROLLIMINE")
küssa = input("Palun siestage parool: ")

check = c.execute(f"""              SELECT *
                                    FROM tabel
                                    WHERE field1 = '{küssa}'""")
if check.fetchone() is not None:
    print("Halb parool")
else:
    print("Hea parool")


ühendus.close()

