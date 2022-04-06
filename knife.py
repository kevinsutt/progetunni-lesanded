print("Sõna nuga esineb; ")
fail = open("csgo.txt", encoding="UTF-8")

for rida in fail:
    if "Knife" in rida:
        print(rida,end="")

fail.close()
