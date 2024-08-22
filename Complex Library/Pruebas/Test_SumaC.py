import unittest 

def SumC(a,b):

    RealP = a[0]+b[0]
    ImaginaryP = a[1] + b[1]

    return RealP, ImaginaryP


class TestSumaC(unittest.TestCase):
    
    def test_suma_complejos_1(self):
        self.assertEqual(SumC([3,-1],[1,4]), (4,3))
        
    def test_suma_complejos_2(self):
        self.assertEqual(SumC([8,-5],[3.5,2]), (11.5,-3))

if __name__ =='__main__':
    unittest.main()
