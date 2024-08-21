import math
import unittest

def Cartesianas_a_polares(a):
    p = (a[0]**2 + a[1]**2)**(1/2)
    teta = math.atan2(a[1],a[0])
    
    return p, teta

    
class Test_Cartesianas_Polares(unittest.TestCase):
    
    def Test_transfromacion_1(self):
        self.assertEqual(Cartesianas_a_polares([1,1]),(2**1/2,math.pi/4))
    
    def Test_transfromacion_2(self):
        self.assertEqual(Cartesianas_a_polares([0,1]),(1,math.pi))      


if __name__ == "__main__":
    
    unittest.main()
