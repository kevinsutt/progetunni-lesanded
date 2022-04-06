t = []
maasikas = "maasikad"
suhkur = "suhkur"
#print(t)
a = []
print("Retseptid, milleks on vaja maasikaid ja suhkrut: ")
file = open('retseptid.txt', 'r', encoding="utf-8").readlines()
for line in file:
    if maasikas in line and suhkur in line:
        line = line.strip()
        print(line.split(","))
