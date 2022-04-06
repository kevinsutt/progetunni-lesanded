fail = open('ukraina.txt', encoding='utf-8')
fail2 = open('vene.txt', encoding='utf-8')

print("Leidsin, et mõlemas keeles on võrdsed need kirjapildid")
i = 0
for line1 in fail:
    for line2 in fail2:
        if line1 == line2:
            print(line1 + line2)
            i = i + 1
        else:
            i = i 
        break
    
print("Kokku leiti " + str(i) + " kattuvust.")    
 
fail.close()
fail2.close()
