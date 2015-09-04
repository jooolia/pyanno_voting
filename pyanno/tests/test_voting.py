import unittest
import numpy as np


from pyanno import voting
MV = -7


class TestVoting(unittest.TestCase):

    def test_labels_count(self):
        annotations = [
            [1,  2, MV, MV],
            [MV, MV,  3,  3],
            [MV,  1,  3,  1],
            [MV, MV, MV, MV],
        ]
        nclasses = 5
        expected = [0, 3, 1, 3, 0]
        result = voting.labels_count(annotations, nclasses, MV)
        self.assertEqual(result, expected)

    def test_majority_vote(self):
        annotations = [
            [1, 2, 2, MV],
            [2, 2, 2, 2],
            [1, 1, 3, 3],
            [1, 3, 3, 2],
            [MV, 2, 3, 1],
            [MV, MV, MV, 3],
        ]
        expected = [2, 2, 1, 3, 1, 3]
        result = voting.majority_vote(annotations, MV)
        self.assertEqual(expected, result)

    def test_majority_vote_empty_item(self):
        # Bug: majority vote with row of invalid annotations fails
        annotations = np.array(
            [[1, 2, 3],
             [MV, MV, MV],
             [1, 2, 2]]
        )
        expected = [1, MV, 2]
        result = voting.majority_vote(annotations, MV)
        self.assertEqual(expected, result)

    def test_sum(self):
	self.assertAlmostEqual(1.1+2.2, 3.3)

    def test_add_arrays(self):
    	x = np.array([1,1])
        y = np.array([2,2])
        z = np.array([3,3])
        np.testing.assert_array_equal(x+y, z)

    def test_labels_frequency(self):
	annotations = np.array([[1, 1, 2], [MV, 1, 2]])
	expected = [ 0. ,  0.6,  0.4,  0. ]
	result =  voting.labels_frequency(annotations, 4, MV)
	print(result)
	np.testing.assert_array_almost_equal(expected, result)

    def test_missing_observations(self):
	annotations = np.array([[MV,MV,MV], [MV, MV, MV]])

	with self.assertRaises(voting.PyannoValueError):
		voting.labels_count(annotations, 4, MV)

    def test_different_missing_value(self):
        annotations = np.array([[1, 1, 2], [MV, 1, 2]])
	expected = [ 0. ,  0.6,  0.4,  0. ]
	result =  voting.labels_frequency(annotations, 4, MV)
	print(result)
	np.testing.assert_array_almost_equal(expected, result)        
		

    def test_proper_missing_value(self):
        self.assertIn(MV,[-1,-999])
		
if __name__ == '__main__':
    unittest.main()
