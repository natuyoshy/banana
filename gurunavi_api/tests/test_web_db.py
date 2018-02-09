import unittest.mock

from mock.mock import MagicMock

from web_db import search_rest, get_freeword


class TestStringMethods(unittest.TestCase):
    def 余分なテスト(self):
        rests = search_rest({
            "rest":
                [{"name": 'name',
                  "latitude": '567',
                  "longitude": '563',
                  "category": 'ggg',
                  "url": 'ggg',
                  "address": 'ggg',
                  "id": 'dd'}
                 ]})

        self.assertListEqual(rests, ['name', '567', '563', 'ggg', 'ggg', 'ggg'])

    def 不足なテスト(self):
        rests = search_rest({
            "rest":
                [{"name": 'name',
                  "latitude": '567',
                  "longitude": '563',
                  "category": 'ggg',
                  "address": 'ggg'}
                 ]})

        self.assertListEqual(rests, ['name', '567', '563', 'ggg', 'ggg'])

    def ぬるテスト(self):
        rests = search_rest({
            "rest":
                [{}
                 ]})

        self.assertListEqual(rests, [])

    def 配列テスト(self):
        rests = search_rest({
            "rest":
                [{"name": 'name',
                  "latitude": '567',
                  "longitude": '563',
                  "category": 'ggg',
                  "address": 'ggg'},
                 {"name": 'names',
                  "latitude": '564',
                  "longitude": '533',
                  "category": 'gd',
                  "address": 'gg'}
                 ]
        })

        self.assertListEqual(rests, [{'name', '567', '563', 'ggg', 'ggg'}, {'names', '564', '533', 'gd', 'gg'}])
        self.assertListEqual(len(rests), 2)

    def フリーワードテスト(self):
        freeword = get_freeword(MagicMock(value="らーめん"))
        assert freeword == ""