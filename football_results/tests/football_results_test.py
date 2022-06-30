import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    
    def setUp(self):
        self.match_1 = {
            "home_score": 0,
            "away_score": 1
        }
        self.second_match = {
            "home_score":1,
            "away_score":0
        }
        self.match_3 = {
            "home_score": 1,
            "away_score": 1
        }

    def test_get_result_0_1_return_away_win(self):
        self.assertEqual("Away win", get_result(self.match_1))

    def test_get_result_1_0_return_home_win(self):
        self.assertEqual("Home win",get_result(self.second_match) )

    def test_get_result_1_1_return_draw(self):
        self.assertEqual("Draw", get_result(self.match_3))
    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 


if __name__ == "__main__":
    unittest.main()


