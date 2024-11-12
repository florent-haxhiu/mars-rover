import unittest
from main import Rover 

class TestRover(unittest.TestCase):

    def setUp(self): 
        self.target = Rover()
        self._obstacles = [(0, 3), (2, 3)]

    def test_going_north_once(self):
        actual = self.target.execute("M")
        expected = "0:1:N"

        self.assertEqual(expected, actual)

    def test_goes_1left_2foward(self):
        actual = self.target.execute("RMM")
        expected = "2:0:E"

        self.assertEqual(expected, actual)

    def test_goes_up_forever(self):
        actual = self.target.execute("MMMMMMMMMM")
        expected = "0:0:N"

        self.assertEqual(expected, actual)

    def test_goes_1right_2forward_1left_1forward(self):
         actual = self.target.execute("RMMLM")
         expected = "2:1:N"

         self.assertEqual(expected, actual)

    def test_goes_2forward_right_and_3forward_left(self):
        actual = self.target.execute("MMRMMLM")
        expected = "2:3:N"

        self.assertEqual(expected, actual)

    def test_goes_4right(self):
        actual = self.target.execute("RRRR")
        expected = "0:0:N"

        self.assertEqual(expected, actual)

    def test_wraps_around(self):
        actual = self.target.execute("RMMMMMMMMMM")
        expected = "0:0:E"

        self.assertEqual(expected, actual)

    def test_hitting_obstacle(self):
        actual = self.target.execute("MMM", self._obstacles)
        expected = "Hit: 0:2:N"
        
        self.assertEqual(expected, actual)

    def test_hits_another_obstacle(self):
        actual = self.target.execute("MMRMMLM", self._obstacles)
        expected = "Hit: 2:2:N"

        self.assertEqual(expected, actual)
