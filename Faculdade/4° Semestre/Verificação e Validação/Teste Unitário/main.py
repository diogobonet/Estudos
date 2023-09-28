# INTEGRANTES: DIOGO BONET, GABRIEL MOCELLIN E VITTORIO CAPRIOLI
import unittest
class Calculadora():
    def Soma(self, a, b):
        return a + b

    def Sub(self, a, b):
        return a - b

    def Mult(self, a, b):
        return a * b

    def Pow(self, a, b):
        return a ** b

    def Div(self, a, b):
        return a / b

    def Module(self, a, b):
        return a % b

class TestCalc(unittest.TestCase):

    def testSoma(self):
        calc = Calculadora()
        resultado = calc.Soma(7, 8)
        self.assertEqual(resultado, 15)
    def testSub(self):
        calc = Calculadora()
        resultado = calc.Sub(1, 3)
        self.assertEqual(resultado, -2)
    def testMult(self):
        calc = Calculadora()
        resultado = calc.Mult(5, 4)
        self.assertEqual(resultado, 20)
    def testPow(self):
        calc = Calculadora()
        resultado = calc.Pow(5, 2)
        self.assertEqual(resultado, 25)
    def testDiv(self):
        calc = Calculadora()
        resultado = calc.Div(25, 5)
        self.assertEqual(resultado, 5)
    def testModulo(self):
        calc = Calculadora()
        resultado = calc.Module(4, 2)
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    teste = TestCalc()

    print("Resultado soma : " + str(teste.testSoma()) )
    print("Resultado subtração : " + str(teste.testSub()) )
    print("Resultado multiplicação : " + str(teste.testMult()) )
    print("Resultado potência : " + str(teste.testPow()) )
    print("Resultado divisão : " + str(teste.testDiv()) )
    print("Resultado módulo : " + str(teste.testModulo()) )
    unittest.main()

