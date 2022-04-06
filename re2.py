import re
sõna = "suvaline"
print (sõna + " ==> " + re.sub(".", "*", sõna))
sõna = input("keelatud sõna: ")
lause = input("Paha lause: ")
if sõna == "":
    print("alusta uuesti")
else:
    print("keelatud sõna: " + sõna)

leib = re.findall("(("+sõna+")\w*)", lause)

print("leiti: " + leib[0][0])

for sõna in sõna:
    lause = re.sub(sõna + "\w*", "*", lause)
print(lause)
