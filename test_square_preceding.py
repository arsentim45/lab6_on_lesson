from unittest import TestCase

from square_preceding import square_preceding

print(square_preceding([1, 2, 3]))


class TestSquare_preceding(TestCase):
    def test_square_preceding(self):
        self.assertEqual(square_preceding([1,2,3]), [0,1,4], 'no')
        self.assertEqual(square_preceding([ ]), [ ], 'no')
        self.assertEqual(square_preceding([9]), [0], 'no')
        self.assertEqual(square_preceding([9,5]), [81], 'no')
        self.fail()
