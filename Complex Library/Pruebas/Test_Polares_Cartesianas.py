import math
import unittest

def PolaresACartesianas(polar):
    
    a = polar[0]*math.cos(polar[1])
    b = polar[0]*math.sin(polar[1])
    
    return a, b 
    
class Test_Polares_Cartesianas(unittest.TestCase):
    
    def Test_transformacion_1(self):
        self.assertEqual(PolaresACartesianas([2**1/2,math.pi/4]),(1,1))
    
    def Test_transformacion_1(self):
        self.assertEqual(PolaresACartesianas([1,math.pi]),(0,1))


if __name__ == "__main__":
    unittest.main()
