fail = open("tulemused" + ".txt", "r")
content = fail.read()
content_list = content.splitlines()
#content_list = content.split()
fail.close()
#print(content_list)
osad = content_list[0].split()
osad1 = content_list[1].split()
osad2 = content_list[2].split()
osad3 = content_list[3].split()
i = 0
j = 0

if int(int(osad[0]) > int(osad[1])):
    i = i + 1
if int(int(osad1[0]) > int(osad1[1])):
    i = i + 1
if int(int(osad2[0]) > int(osad2[1])):
    i = i + 1
else:
    j = j + 1
if int(int(osad3[0]) > int(osad3[1])):
    i = i + 1

print("Eesti võitis " + str(i) + "-" + str(j))
