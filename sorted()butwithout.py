listike = [1020, 25, 12, 46, 11, 2 ,299, 44,3, 522, 234, 14]

for i in range(len(listike)):
    for k in range(i + 1, len(listike)):
        if listike[i] > listike[k]:
           listike[i],listike[k] = listike[k],listike[i]
print(listike)
