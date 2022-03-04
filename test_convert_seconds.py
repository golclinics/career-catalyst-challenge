import unittest
from random import randint
from convert_seconds import my_function

class TestConvertSeconds(unittest.TestCase):
    '''
        Test that shows the conversion of minutes to strings.
    '''
    def test_right_ans(self):
        # testing the correct value
        value = randint(0,6)
        result = my_function(value)
        self.assertEqual(result,value*60)

    def test_wrong_data_type(self):
        # testing wrong data type
        value = 'v'
        result = my_function(value)
        self.assertNotIsInstance(result,int)
        self.assertEqual(result,"Value should be an int")
    
    def test_wrong_ans(self):
        # testing the wrong result
        value = randint(0,60)
        result = my_function(value)
        self.assertIsNot(result,value*randint(0,59))

if __name__ =="__main__":
    unittest.main()