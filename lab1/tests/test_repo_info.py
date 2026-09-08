import unittest

from lab1.repo_info import format_summary, parse_shortlog


class ParseShortlogTests(unittest.TestCase):

    def test_parses_tab_separated_output(self):
        text = '     5\tRobertoKarlol\n     2\tИван Иванов\n'
        self.assertEqual(
            parse_shortlog(text),
            [('RobertoKarlol', 5), ('Иван Иванов', 2)],
        )

    def test_parses_space_separated_output(self):
        self.assertEqual(parse_shortlog('12 Ada Lovelace'),
                         [('Ada Lovelace', 12)])

    def test_skips_blank_lines(self):
        self.assertEqual(parse_shortlog('\n\n  \n'), [])


class FormatSummaryTests(unittest.TestCase):

    def test_lists_every_author(self):
        summary = format_summary('feature', 7, [('Ada', 4), ('Grace', 3)])
        self.assertIn('Текущая ветка: feature', summary)
        self.assertIn('Всего коммитов: 7', summary)
        self.assertIn('  Ada: 4', summary)
        self.assertIn('  Grace: 3', summary)

    def test_works_without_authors(self):
        self.assertEqual(
            format_summary('main', 0, []),
            'Текущая ветка: main\nВсего коммитов: 0\nАвторы:',
        )


if __name__ == '__main__':
    unittest.main()
