import unittest


class Submarino():
    
    def __init__(self):
        self.bussola = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.direcoes = {
            0: "NORTE", 
            1: "LESTE", 
            2: "SUL", 
            3: "OESTE"
        }

    def direita(self):
        self.bussola = 0 if self.bussola == 3 else self.bussola + 1
        return self.bussola

    def esquerda(self):
        self.bussola = 3 if self.bussola == 0 else self.bussola - 1
        return self.bussola
    
    def baixo(self):
        self.z = self.z - 1
        return self.z

    def cima(self):
        self.z = 0 if self.z == 0 else self.z + 1
        return self.z

    def direcao(self):
        return self.direcoes.get(self.bussola)

    def posicao(self):
        lista = [str(self.x), str(self.y), str(self.z), self.direcao()] 
        return " ".join(lista)

    def movimenta(self):
        if self.direcoes.get(self.bussola) == "LESTE":
            self.x += 1
        elif self.direcoes.get(self.bussola) == "OESTE":
            self.x -= 1
        elif self.direcoes.get(self.bussola) == "NORTE":
            self.y += 1
        else:
            self.y -= 1

    def coordenada(self, instrucao=""):
        comandos = [c for c in instrucao]

        for c in comandos:
            if c == "R":
                self.direita()
            elif c == "L":
                self.esquerda()
            elif c == "D":
                self.baixo()
            elif c == "U":
                self.cima()
            elif c == "M":
                self.movimenta()

        return self.posicao()


class SubmarinoTest(unittest.TestCase):

    '''
          NORTE
            0
    OESTE       LESTE
      3           1
           SUL
            2
    '''
    def test_posicionamento(self):
        sub = Submarino()

        self.assertEqual(0, sub.bussola)
        self.assertEqual(3, sub.esquerda())
        self.assertEqual(0, sub.direita())
        self.assertEqual(1, sub.direita())
        self.assertEqual(2, sub.direita())
        self.assertEqual(3, sub.direita())

        self.assertEqual(0, sub.z)
        self.assertEqual(-1, sub.baixo())
        self.assertEqual(0, sub.cima())
        self.assertEqual(0, sub.cima())

    def test_orientacao(self):
        sub = Submarino()

        self.assertEqual("NORTE", sub.direcao())
        sub.esquerda()
        self.assertEqual("OESTE", sub.direcao())
        sub.esquerda()
        self.assertEqual("SUL", sub.direcao())
        sub.esquerda()
        self.assertEqual("LESTE", sub.direcao())

    def test_posicao_inicial(self):
        sub = Submarino()
        self.assertEqual("0 0 0 NORTE", sub.posicao())

    def test_coordenada_exemplo_1(self):
        sub = Submarino()
        self.assertEqual("2 3 -2 SUL", sub.coordenada("RMMLMMMDDLL"))
    
    def test_coordenada_exemplo_2(self):
        sub = Submarino()
        self.assertEqual("-1 2 0 NORTE", sub.coordenada("LMRDDMMUU"))
    
    def test_coordenada_exemplo_3(self):
        sub = Submarino()
        self.assertEqual("3 -2 -2 SUL", sub.coordenada("RUDDLLLLMMMRMM"))
    

if __name__ == "__main__":
    unittest.main()
