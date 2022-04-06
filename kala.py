kalad = int(input("Kala püütud: "))
print("Teil on " + str(kalad) + " kala")
i = 0
a = 1
summa = 0
list1 = []
while i < kalad:
    numbrid = int(input("Kala " + str(a) + " kaal on: "))
    list1.append(numbrid)
    summa = summa + numbrid
    i = i + 1
    a = a + 1
   


print("Keskmine kala on " + str(round(summa/kalad)))
print(min(list1))
print(max(list1))
