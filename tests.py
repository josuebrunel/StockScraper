import logging

from unittest import TestCase

logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s %(levelname)s] [%(name)s.%(module)s.%(funcName)s] %(message)s \n")
logging.getLevelName('Test-StockScraper')

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
        logging.debug(data)

    def test_get_hisorical_info_without_params(self):

        data = get_historical_info('YHOO')
        logging.debug(data)
