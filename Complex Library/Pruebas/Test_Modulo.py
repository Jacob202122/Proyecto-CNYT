import unittest

def Modulo(a):
    r = (a[0]**2 + a[1]**2)**(1/2)
    
    return r

class TestModulo(unittest.TestCase):
    
    def test_modulo_1(self):
        self.assertEqual(Modulo([4,3]),5)
    
    def test_modulo_1(self):
        self.assertEqual(Modulo([6,8]),10)
        
if __name__ == '__main__':
    unittest.main()

