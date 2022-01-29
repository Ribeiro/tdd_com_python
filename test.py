# -*- coding: utf-8 -*-
import unittest
from juros import Juros


# Formula Calculo de Juros Simples - J = C.i.n
# Onde
# J = juros
# C = capital
# i = taxa de empréstimo
# n = períodos


class MyCalcTest(unittest.TestCase):
    def testSimples(self):
        calcJuros = Juros()
        calcJuros.capital = 16000
        calcJuros.taxa = 0.04
        calcJuros.n_periodos = 4

        self.assertEqual(2560, calcJuros.simples())


if __name__ == '__main__':
    unittest.main()
