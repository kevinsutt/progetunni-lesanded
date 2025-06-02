n = float(input("Nimetage arv: "))  # küsime arvu

def faktoriaal(n): # leiame arvu faktoriaal
    if n < 0:
        return "Faktoriaal ei ole defineeritud negatiivsete arvude jaoks"
    elif not n.is_integer():
        return "Faktoriaal on defineeritud ainult täisarvude jaoks"
    elif n == 0:
        return 1
    else:
        return faktoriaal(n - 1) * n

print("Tulemus:", faktoriaal(n)) # kuvame lõpptulemust
