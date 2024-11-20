import math
import paddle
import unitest
import numpy as np



class TestConstantNanInf(unitest.TestCase):

    def TestConstantNan(self):
        #self.assertEqual(math.nan, paddle_nan)
        x = np.array([paddle.nan])
        np.testing.assert_equal(repr(x), 'array([nan])')
    
    def TestConstantInf(self):
        x = np.array([paddle.inf])
        np.testing.assert_equal(repr(x), 'array([inf])')

if __name__ == '__main__':
    unittest.main()









