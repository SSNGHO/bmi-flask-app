import unittest

from app import app


class IndexRouteTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("테트리스".encode("utf-8"), response.data)

    def test_index_contains_board_canvas(self):
        response = self.client.get("/")
        html = response.data.decode("utf-8")
        self.assertIn('id="board"', html)
        self.assertIn('id="next"', html)


if __name__ == "__main__":
    unittest.main()
