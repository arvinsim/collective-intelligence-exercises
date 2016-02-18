import unittest
from math import sqrt
from data import critics
from euclidean_distance_score import get_euclidean_distance, sim_distance

class TestMakingRecommendations(unittest.TestCase):
    # TODO: Implement
    def test_euclidean_distance_book(self):
        result = 1/(1+sqrt(
            pow(
                critics['Mick LaSalle']['Snakes on a Plane']
                -
                critics['Toby']['Snakes on a Plane']
                ,2
            )
            +
            pow(
                critics['Mick LaSalle']['You, Me and Dupree']
                -
                critics['Toby']['You, Me and Dupree']
                ,2
            )
        ))

        # print(result)
        # print(sim_distance(critics, 'Toby', 'Mick LaSalle'))
        # print(sim_distance(critics, 'Mick LaSalle', 'Toby'))
        # print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))

    def test_euclidean_distance_mine(self):
        Angel = {
            'movie1': 1,
            'movie2': 5,
            'movie3': 1
        }

        Bernard = {
            'movie1': 1,
            'movie2': 4,
            'movie3': 3
        }

        Claudia = {
            'movie1': 3,
            'movie2': 2,
            'movie4': 4
        }

        Devon = {
            'movie1': 1,
            'movie2': 5,
            'movie3': 1
        }

        # print(get_euclidean_distance(Angel, Bernard))
        # print(get_euclidean_distance(Angel, Claudia))
        # print(get_euclidean_distance(Angel, Devon))

        self.assertEqual(get_euclidean_distance(Angel, Devon), 1)

if __name__ == '__main__':
    unittest.main()
