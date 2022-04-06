# Teha programm, mis küsib kasutajalt faili laiendi (csv, txt, json, ... vms) ja liidab üheks suureks failiks kõik jooskvas kaustas olevad selle laiendiga failid.
# asukoht
küssa = input("Asukoht: ")
import os, glob
import os.path
from pathlib import Path
#path = r"C:\tmp"
path = r""+ str(küssa) + ""
os.chdir(path)
retval2 = os.getcwd()
print("Asukoht on %s" % retval2)
# faili laiendi küsimus
küsimus = input("Faili laiend: ")

if küsimus == küsimus:
    if küsimus.startswith("."):
        print("Sa oled valinud " + str(küsimus))
    else:
        print("Sa oled valinud " + str(küsimus))
        print("See ei ole faili laiend")          
if küsimus == ".":
    print("Leidub ainult punkt, kus on ülejäänud?")
d = küsimus.count(".")
if d > 1:
    print("Liiga palju punkte!")    
# liidame üheks suureks failiks kõik jooksvas kaustas olevad selle laiendiga failid
# leiame failid
# liita kokku saame ainult tekstilisi faile ehk text document.
# .txt on teksti dokumendid
i = 0
listt = []
for file in glob.glob("*" + str(küsimus)):
    print("Leitud fail: " + str(file))
    i = i + 1
    listt.append(küsimus)
print("Kokku on " + str(i) + " fail(i).")
listt = (glob.glob("*" + str(küsimus)))
#print(listt)
j = 0
while j < i:
    with open('suurfail.txt', 'w') as outfile:
        for fail in listt:
            with open(fail) as infile:
                outfile.write(infile.read())
                outfile.write("\n")
                j = j + 1
