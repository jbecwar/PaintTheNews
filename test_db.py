import unittest
from unittest.mock import patch, MagicMock
import db

class TestDBFunctions(unittest.TestCase):
    @patch('db.sqlite3.connect')
    def test_createHeadlineTable(self, mock_connect):
        # Mock the connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Call the function
        db.createHeadlineTable()

        # Check that the database functions were called correctly
        mock_connect.assert_called_once_with('paint_the_news.db')
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with('''CREATE TABLE headlines IF NOT EXISTS (id INTEGER PRIMARY KEY AUTOINCREMENT, source TEXT, title TEXT, url TEXT, date TEXT)''')
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('db.sqlite3.connect')
    def test_insertHeadline(self, mock_connect):
        # Mock the connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Call the function
        db.insertHeadline('source', 'title', 'url', 'date')

        # Check that the database functions were called correctly
        mock_connect.assert_called_once_with('paint_the_news.db')
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with('''INSERT INTO headlines (source, title, url, date) VALUES (?, ?, ?, ?)''', ('source', 'title', 'url', 'date'))
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()