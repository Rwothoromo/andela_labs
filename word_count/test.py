from unittest import TestCase
from word_count import *

# For example for the input "olly olly in come free"

# olly: 2
# in: 1
# come: 1
# free: 1

class TestWordCounts(TestCase):

    """
        Counts the occurrences or characters in a word
    """

    def test_word_occurance1(self):
        self.assertDictEqual(
            {'word': 1},
            words('word'),
            msg='should count one word'
        )

    def test_word_occurance2(self):
        self.assertDictEqual(
            {'one': 1, 'of': 1, 'each': 1},
            words("one of each"),
            msg='should count one of each'
        )

    def test_word_occurance3(self):
        self.assertDictEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            words("one fish two fish red fish blue fish"),
            msg='should count multiple occurrences'
        )

    def test_word_occurance4(self):
        self.assertDictEqual(
            {'car': 1, ":": 2, 'carpet': 1, 'as': 1, 'java': 1, 'javascript!!&@$%^&': 1},
            words('car : carpet as java : javascript!!&@$%^&'),
            msg='should include punctuation'
        )

    def test_word_occurance5(self):
        self.assertDictEqual(
            {'testing': 2, 1: 1, 2: 1},
            words('testing 1 2 testing'),
            msg='should include numbers'
        )

    def test_word_occurance6(self):
        self.assertDictEqual(
            {'go': 1, 'Go': 1, 'GO': 1},
            words('go Go GO'),
            msg='should respect case'
        )

    def test_word_occurance7(self):
        self.assertDictEqual(
            {"¡Hola!": 1, "¿Qué": 1, "tal?": 1, "??????!": 1},
            words('¡Hola! ¿Qué tal? ??????!'),
            msg='should count international characters properly'
        )

    def test_word_occurance8(self):
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello\nworld'),
            msg='should not count multilines'
        )

    def test_word_occurance9(self):
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello\tworld'),
            msg='should not count tabs'
        )

    def test_word_occurance0(self):
        self.assertDictEqual(
            {'hello': 1, 'world': 1},
            words('hello  world'),
            msg='should count multiple spaces as one'
        )


