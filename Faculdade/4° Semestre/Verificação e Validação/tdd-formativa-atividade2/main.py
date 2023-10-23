import unittest

class Calculadora():
    def areaRetang(self, comprimento, largura):
        return comprimento * largura

# Código de teste seguindo o método de testes TDD
class Teste(unittest.TestCase):
    def test(self):
        calc = Calculadora()
        resultado = calc.areaRetang(12, 12)
        return self.assertEqual(resultado, 144)
    
if __name__ == '__main__':
    teste = Teste()
    unittest.main()
