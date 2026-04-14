import unittest

from src.python_demo_package_9999.demo import roll


class TestRoll(unittest.TestCase):
    def test_roll_string(self):
        """
        Test that the roll function returns a string.
        """
        result = roll()
        self.assertIsInstance(result, str, "The result should be a string.")

    def test_roll_structure(self):
        """
        Test that the roll function returns a string that starts with "The answer is: ".
        """
        result = roll()
        self.assertTrue(
            result.startswith("The answer is: "),
            "The result should start with 'The answer is: '.",
        )
    
    def test_benchmark_roll(self):
        """
        Benchmark the roll function to ensure it runs within a reasonable time frame.
        """
        import time
        start_time = time.time()
        roll()
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 1, "The roll function should execute in less than 1 second.")


if __name__ == "__main__":
    unittest.main()
