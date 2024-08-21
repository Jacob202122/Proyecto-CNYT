import unittest

def Conjugado(a):
    
    RealP = a[0]
    ImaginaryP = -a[1]

    return RealP, ImaginaryP

class TestConjugado(unittest.TestCase):
    
    def Test_Conjugado_1(self):
        self.assertEqual(Conjugado([1,2]),(1,-2))
    
    def Test_Conjugado_2(self):
        self.assertEqual(Conjugado([7,-2]),(7,2))


if __name__ == '__main__':
    unittest.main()
