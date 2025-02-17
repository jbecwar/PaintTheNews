import unittest
from ai import removeCommonWords

class TestRemoveCommonWords(unittest.TestCase):
    def test_remove_common_words(self):
        prompt = "this is a test prompt with some common words"
        expected_result = "test prompt common words"
        self.assertEqual(removeCommonWords(prompt), expected_result)

    def test_remove_common_words_with_capitals(self):
        prompt = "This Is A Test Prompt WIth Some Common Words"
        expected_result = "Test Prompt Common Words"
        self.assertEqual(removeCommonWords(prompt), expected_result)

    def test_remove_common_words_empty(self):
        prompt = ""
        expected_result = ""
        self.assertEqual(removeCommonWords(prompt), expected_result)

    def test_remove_common_words_no_common(self):
        prompt = "unique words"
        expected_result = "unique words"
        self.assertEqual(removeCommonWords(prompt), expected_result)

if __name__ == '__main__':
    unittest.main()