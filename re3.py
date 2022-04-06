import re

pahad_sõnad = ["piim|piimapea", "mets|metsa"]
#lause = "Siin on lause, kust tuleb eemaldada sõnad piimapea ja metsa."
#Tulemus: Siin on lause, kust tuleb eemaldada sõnad ******** ja *****.

sõna = "halb sõna"
print(sõna + " ==> " + re.sub(".", "*", sõna))
lause = "Siin on lause, kust tuleb eemaldada sõnad piimapea ja metsa."
lause2 = " metsa."
paha_sõna = "piimapea"
paha_sõna2 = "metsa"

obamnium = ["sõna"]
#print(re.sub("(("+paha_sõna+")("+paha_sõna2+")\w*)", "*", lause))
leid = re.findall("(("+paha_sõna+")\w*)", lause)
leid2 = re.findall("(("+paha_sõna2+")\w*)", lause)
print("Leiti: " + leid[0][0] + " ja " + leid2[0][0] + ".")
for sõna in obamnium:
    lause = "Siin on lause, kust tuleb eemaldada sõnad piimapea ja"
    lause2 = " metsa."
    daa = (re.sub("(("+paha_sõna+")\w*)", "*"*8, lause))
    saa = (re.sub("(("+paha_sõna2+")\w*)", "*"*5, lause2))
    faa = daa + saa
    print(faa)
