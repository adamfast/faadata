from django.test import TestCase
from faadata.airports.utils import *

class AirportTests(TestCase):
    fixtures = ['airports.json']

    def test_decide_k(self):
        self.assertEqual(decide_k('EOS'), 'EOS')
        self.assertEqual(decide_k('KEOS'), 'EOS')
        self.assertEqual(decide_k('K81'), 'K81')
        self.assertEqual(decide_k('KKKI'), 'KKI')
        self.assertEqual(decide_k('KKI'), 'KKI')
        self.assertEqual(decide_k('KKLS'), 'KLS')
        self.assertEqual(decide_k('KLS'), 'KLS')
