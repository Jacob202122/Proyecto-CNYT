import unittest

def MultC(a,b):

    Realp = a[0]*b[0] - a[1]*b[1]
    ImaginaryP = a[0]*b[1] + a[1]*b[0]

    return Realp, ImaginaryP


class TestProductoC (unittest.TestCase):
    
    def test_producto_1(self):
        self.assertEqual(MultC([3,-1],[1,4]),(7,11))
    
    def test_producto_2(self):
        self.assertEqual(MultC([3,-2],[1,2]),(7,4))


if __name__ == "__main__":
    
    unittest.main()
