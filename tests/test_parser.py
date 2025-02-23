import unittest

from entry_parser import EntryParser


class TestEntryParser(unittest.TestCase):
    def test_single_list_entry(self):
        entry = "[1, 2, 3]"
        expected_result = [["1", "2", "3"]]
        p = EntryParser(entry)
        p.parse()
        self.assertEqual(p.result, expected_result)

    def test_multiple_lists_entry_comma_separated(self):
        entry = "[1, 2, 3],[4, 5, 6]"
        expected_result = [["1", "2", "3"], ["4", "5", "6"]]
        p = EntryParser(entry)
        p.parse()
        self.assertEqual(p.result, expected_result)

    def test_multiple_lists_entry_whitespace_separated(self):
        entry = "[1, 2, 3] [4, 5, 6]"
        expected_result = [["1", "2", "3"], ["4", "5", "6"]]
        p = EntryParser(entry)
        p.parse()
        self.assertEqual(p.result, expected_result)

    def test_multiple_lists_entry_comma_whitespace_separated(self):
        entry = "[1, 2, 3], [4, 5, 6]"
        expected_result = [["1", "2", "3"], ["4", "5", "6"]]
        p = EntryParser(entry)
        p.parse()
        self.assertEqual(p.result, expected_result)

    def test_multiple_lists_entry_junk_separated(self):
        entry = "[1, 2, 3] adf dafd  fd,,, , af , , fdf [4, 5, 6]"
        expected_result = [["1", "2", "3"], ["4", "5", "6"]]
        p = EntryParser(entry)
        p.parse()
        self.assertEqual(p.result, expected_result)

    def test_values_whitespace_separated(self):
        entry = "[1 2 3] [4 5 6]"
        expected_result = [["123"], ["456"]]
        p = EntryParser(entry)
        p.parse()
        self.assertEqual(p.result, expected_result)

    def test_invalid_separator_separated(self):
        entry = "[1.2.3]"
        expected_result = [["123"]]
        p = EntryParser(entry)
        p.parse()
        self.assertEqual(p.result, expected_result)

    def test_combined_values(self):
        entry = "[12, abc, 34], [445, 5, 6567]"
        expected_result = [["12", "abc", "34"], ["445", "5", "6567"]]
        p = EntryParser(entry)
        p.parse()
        self.assertEqual(p.result, expected_result)

    def test_skip_whitespace_start_list_entry(self):
        entry = " [1, 2, 3]"
        expected_result = [["1", "2", "3"]]
        p = EntryParser(entry)
        p.parse()
        self.assertEqual(p.result, expected_result)

    def test_skip_invalid_chars_list_entry(self):
        entry = "1334 adgdfa [1, 2, 3]"
        expected_result = [["1", "2", "3"]]
        p = EntryParser(entry)
        p.parse()
        self.assertEqual(p.result, expected_result)

    def test_invalid_unclosed_list_entry(self):
        entry = "[1, 2, 3"
        with self.assertRaises(ValueError):
            EntryParser(entry)

    def test_invalid_no_list_entry(self):
        entry = "1, 2, 3"
        with self.assertRaises(ValueError):
            EntryParser(entry)

    def test_invalid_unopened_list_entry(self):
        entry = "1, 2, 3]"
        with self.assertRaises(ValueError):
            EntryParser(entry)
