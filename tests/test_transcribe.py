import unittest
from app import create_app

class TestTranscribeRoute(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_transcribe_no_file(self):
        response = self.client.post("/transcribe/")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Audio file is required", response.get_json()["error"])
