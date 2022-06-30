import unittest

from src.high_scores import latest, ordered_highest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.list= [22, 34, 11, 6, 78]
        self.list2 = sorted(self.list, reverse=True)
        self.list3 = [17, 33, 24, 4, 26, 24]
        self.list4 = [12 ,16]
        self.list5 = [1]
    # Tests

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(78, latest(self.list))
    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(78,personal_best(self.list))
    # Test top three from list of scores
    def test_top_three_from_list(self):
        self.assertEqual([78, 34, 22],personal_top_three(self.list) )

    # Test ordered from highest tp lowest
    def test_ordered_from_highest_to_lowest(self):
        self.assertEqual(True, ordered_highest(self.list))
    # Test top three when there is a tie
    def test_top_three_if_tie(self):
        self.assertEqual([33, 26, 24], personal_top_three(self.list3))
    # Test top three when there are less than three
    def test_top_three_if_less_than_three(self):
        self.assertEqual([16, 12], personal_top_three(self.list4))
    # Test top three when there is only one
    def test_top_three_when_there_is_only_one(self):
        self.assertEqual([1], personal_top_three(self.list5))
