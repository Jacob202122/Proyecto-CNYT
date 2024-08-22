import math
import unittest


def fase(a):
    
    teta = math.atan2(a[1],a[0])
    
    return teta
    
class TestFase(unittest.TestCase):
    
    def test_fase_1(self):
        self.assertEqual(fase([1,1]), math.pi/4)
    
    def test_fase_1(self):
        self.assertEqual(fase([-1,0]), math.pi)

if __name__ == "__main__":
    
    unittest.main()
