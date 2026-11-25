import unittest
from cache_lab.cli import run_demo

class CacheLabTests(unittest.TestCase):
    def test_repeated_call_adds_a_hit(self):
        result = run_demo(10, 4)
        self.assertGreater(result["after_repeat"]["hits"], result["after_first_call"]["hits"])

    def test_typed_keys_are_distinct(self):
        result = run_demo(8, 3)
        self.assertEqual(result["typed_keys"], {"int_1": "int", "float_1_0": "float"})

if __name__ == "__main__":
    unittest.main()
