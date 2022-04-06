from random import randint
vale = 0
# 50/50 peab olema valik + voi *
# ketra lõputult
while True:
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 2)
    jrk = 0
   
   
    if c == 1:
        vastus = int(input("Arvuta " + str(a) + "*" + str(b) + "="))
        if vastus == a*b:
            print("Õige! Vastasid " + str(vale) + " korda valesti.")
            break
        else:
            print("Vale!")
            vale = vale + 1
           
    elif c == 2:
            vastus = int(input("Arvuta " + str(a) + "+" + str(b) + "="))
            if vastus == a+b:
                print("Õige! Vastasid " + str(vale) + " korda valesti.")
                break
            else:
                print("Vale!")
                vale = vale + 1
