from unittest import TestCase

from stockretriever import *

class TestStockRetriever(TestCase):
    """TestCase class for stock retriever
    """

    def setUp(self,):
        pass

    def tearDown(self,):
        pass

    def test_get_hisorical_info_with_new_params(self):

        data = get_historical_info('YHOO',['Open','Close','High','Low'],startDate='2014-09-11',endDate='2015-02-10',limit=5)
        print(data)

    def test_get_hisorical_info_without_params(self):

        data = get_historical_info('YHOO')
        print(data)
