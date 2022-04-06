class Laul:
    def __init__(self, pealkiri, esitaja, vaatamisarv):
        self.pealkiri = pealkiri
        self.esitaja = esitaja
        self.vaatamisarv = vaatamisarv


    def näita(self):
        print(" - " + self.esitaja + ' "' + self.pealkiri + '"' + ' ' + self.vaatamisarv)
