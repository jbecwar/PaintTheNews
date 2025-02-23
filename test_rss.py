import unittest
from unittest.mock import patch, MagicMock
from rss import getTitles

class TestGetTitles(unittest.TestCase):
    @patch('rss.feedparser.parse')
    @patch('rss.db')
    def test_get_titles(self, mock_db, mock_feedparser):
        # Mock the feedparser.parse return value
        mock_feed = MagicMock()
        mock_feed.entries = [
            MagicMock(title='Title 1', link='Link 1', published='01/01/2022'),
            MagicMock(title='Title 2', link='Link 2', published='12/31/2025')
        ]
        mock_feedparser.return_value = mock_feed

        # Call the function
        titles = getTitles()

        # Check that the database functions were called correctly
        mock_db.insertHeadline.assert_any_call('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml', 'Title 1', 'Link 1', '01/01/2022')
        mock_db.insertHeadline.assert_any_call('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml', 'Title 2', 'Link 2', '12/31/2025')

        # Check the return value
        self.assertEqual(titles, ['Title 1', 'Title 2'])

if __name__ == '__main__':
    unittest.main()