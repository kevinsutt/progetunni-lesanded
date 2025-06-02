def kuulikud(kuud): # leiame küülikute paaride arv
    if kuud == 0 or kuud == 1:
        return 1
    else:
        return kuulikud(kuud - 1) + kuulikud(kuud - 2)

sisend = input("Sisestage kuude arv: ")
try:
    kuud = int(sisend)
    if kuud < 0:
        print("Kuude arv peab olema positiivne")
    else:
        print("Küülikupaare:", kuulikud(kuud))
except ValueError:
    print("Sisend peab olema täisarvuline")
