import unittest

def DivC(a,b):
    
    RealP = (a[0]*b[0] + a[1]*b[1])/(b[0]**2 + b[1]**2)
    ImaginaryP = (a[1]*b[0] - a[0]*b[1])/(b[0]**2 + b[1]**2)

    return RealP, ImaginaryP

class testDivC(unittest.TestCase):
    
    def test_DivC_1(self):
        self.assertEqual(DivC([-2,1],[1,2]),(0,1))
        
    def test_DivC_2(self):
        self.assertEqual(DivC([0,1],[1,2]),(0.4,0.2))

if __name__ == "__main__":
    
    unittest.main()
