class Baralho():

    def __init__(self, joker=0):
        self.baralho = []
        self.naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
        for i in range(4):
            for j in range(13):
                carta = [(j+1), self.naipes[i]]
                self.baralho.append(carta)
        for i in range(joker):
            self.baralho.append(['Coringa'])
