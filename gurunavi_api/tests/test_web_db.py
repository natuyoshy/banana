import unittest
from web_db import search_rest


class TestStringMethods(unittest.TestCase):
    def test_search_rest(self):
        rests = search_rest({
            "rest":
                [{"name": 'name',
                  "latitude": '567',
                  "longitude": '563',
                  "category": 'ggg',
                  "url": 'ggg',
                  "address": 'ggg'}
                 ]})
        self.assertListEqual(rests, ['name', '567', '563', 'ggg','ggg', 'ggg'])

        if __name__ == '__main__':
            unittest.main()
