import unittest
import assessment1


class TestPythonLoopsAssessment(unittest.TestCase):

    def test_sum_to_n(self):
        self.assertEqual(assessment1.sum_to_n(1), 1)
        self.assertEqual(assessment1.sum_to_n(5), 15)
        self.assertEqual(assessment1.sum_to_n(10), 55)

    def test_count_even_numbers(self):
        self.assertEqual(assessment1.count_even_numbers(1), 0)
        self.assertEqual(assessment1.count_even_numbers(10), 5)
        self.assertEqual(assessment1.count_even_numbers(9), 4)

    def test_factorial(self):
        self.assertEqual(assessment1.factorial(1), 1)
        self.assertEqual(assessment1.factorial(5), 120)
        self.assertEqual(assessment1.factorial(6), 720)

    def test_multiplication_table(self):
        self.assertEqual(
            assessment1.multiplication_table(3),
            [3,6,9,12,15,18,21,24,27,30]
        )
        self.assertEqual(
            assessment1.multiplication_table(5),
            [5,10,15,20,25,30,35,40,45,50]
        )

    def test_sum_of_digits(self):
        self.assertEqual(assessment1.sum_of_digits(1234), 10)
        self.assertEqual(assessment1.sum_of_digits(1111), 4)
        self.assertEqual(assessment1.sum_of_digits(90), 9)

    def test_count_vowels(self):
        self.assertEqual(assessment1.count_vowels("hello"), 2)
        self.assertEqual(assessment1.count_vowels("python"), 1)
        self.assertEqual(assessment1.count_vowels("AEIOU".lower()), 5)

    def test_find_primes(self):
        self.assertEqual(assessment1.find_primes(10), [2,3,5,7])
        self.assertEqual(assessment1.find_primes(2), [2])
        self.assertEqual(assessment1.find_primes(20), [2,3,5,7,11,13,17,19])

    def test_reverse_string(self):
        self.assertEqual(assessment1.reverse_string("hello"), "olleh")
        self.assertEqual(assessment1.reverse_string("python"), "nohtyp")
        self.assertEqual(assessment1.reverse_string("a"), "a")

    def test_pyramid_pattern(self):
        self.assertEqual(
            assessment1.pyramid_pattern(3),
            ["*", "**", "***"]
        )
        self.assertEqual(
            assessment1.pyramid_pattern(1),
            ["*"]
        )

    def test_multiplication_grid(self):
        self.assertEqual(
            assessment1.multiplication_grid(3),
            [
                [1,2,3],
                [2,4,6],
                [3,6,9]
            ]
        )
        self.assertEqual(
            assessment1.multiplication_grid(2),
            [
                [1,2],
                [2,4]
            ]
        )


if __name__ == "__main__":
    unittest.main()