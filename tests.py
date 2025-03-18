import unittest
from unittest.mock import patch, MagicMock
import main  # Import your main script

class TestMainFunction(unittest.TestCase):

    @patch("main.spotify_client.getSongs")  # Mock the Spotify function
    @patch("main.getFromYT.getLinks")  # Mock the YouTube search function
    @patch("main.yt_downloader.installer")  # Mock the downloader
    @patch("sys.argv", ["main.py", "https://open.spotify.com/playlist/3NEPhttOiDgCrm3r9weldF?si=c88a83c2349248f0", "mp3"])
    def test_main_valid_input(self, mock_installer, mock_getLinks, mock_getSongs):
        """ Test main function with valid inputs """

        # Mock Spotify API response
        mock_getSongs.return_value = [
            {"Song Name": "Song 1", "Artists": "Artist 1"},
            {"Song Name": "Song 2", "Artists": "Artist 2"}
        ]

        # Mock YouTube link response
        mock_getLinks.return_value = [
            "https://www.youtube.com/watch?v=example1",
            "https://www.youtube.com/watch?v=example2"
        ]

        # Run main function
        result = main.main()

        # Assertions
        self.assertEqual(result, None)  # No errors should return None
        mock_getSongs.assert_called_once_with(playlist_ID="3NEPhttOiDgCrm3r9weldF")
        mock_getLinks.assert_called_once()
        mock_installer.assert_called_once_with(
            ["https://www.youtube.com/watch?v=example1", "https://www.youtube.com/watch?v=example2"], "mp3"
        )

    @patch("sys.argv", ["main.py"])
    def test_main_no_arguments(self):
        """ Test if error is thrown when no arguments are provided """
        with patch("builtins.print") as mock_print:
            result = main.main()
            mock_print.assert_called_with('Error: \nUse command: \npython3 main.py <Spotify_Playlist_Link> <mp4 or mp3>')
            self.assertEqual(result, -1)

    @patch("sys.argv", ["main.py", "invalid_url"])
    def test_main_invalid_url(self):
        """ Test if function handles invalid URL formats """
        with patch("builtins.print") as mock_print:
            result = main.main()
            mock_print.assert_called()  # Check if any error message was printed
            self.assertEqual(result, -1)  # Ensure it returns an error

if __name__ == "__main__":
    unittest.main()
