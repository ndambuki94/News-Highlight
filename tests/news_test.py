import unittest
from models import movie
New = new.New

class NewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        

    def test_instance(self):
        self.assertTrue(isinstance(self.new_new,New))


if __name__ == '__main__':
    unittest.main()