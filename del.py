#Teha Pythoni programm, mis suudaks kustutada kõik "a"-tähega algavad failid kaustast "c:\tmp"
# import ja desti leidmine
import os, glob
path = r"C:\tmp"
os.chdir(path)
retval2 = os.getcwd()
print("Asukoht on %s" % retval2)
print("Kustutame kõik failid, mis algavad a tähega.")
# faili kustutamine

for fname in os.listdir(retval2):
    if fname.startswith("a"):
        os.remove(os.path.join(path, fname))
