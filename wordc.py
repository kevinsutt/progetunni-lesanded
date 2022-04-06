wordcount=0
charcount=0
küsimus = str(input("Sisestage string: "))
splitt = küsimus.split()
wordcount = len(splitt)
def split(splitt):
    return [char for char in küsimus]

length = (split(splitt))
no_spaces = []
for rida in length:
    if rida.strip():
        no_spaces.append(rida)
print("Sõnade arv: ",wordcount)
print("Tähtede arv: ", len(no_spaces))
print("Tühikute arv: ",(wordcount-1))
