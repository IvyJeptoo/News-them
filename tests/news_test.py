import unittest
from app.models import Headlines, Sources


class HeadlinesTest(unittest.TestCase):
    '''
    test to test the new headline class behaviour
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_Headline = Headlines('Amina Hassan','imani','Arabia Queens','Fall of the lovely three sisters','www.queen.com','www.urltoimage','Published at:2022-05-02T14:15:00Z')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_Headline,Headlines))
        

class Sources (unittest.TestCase):
    '''
    test to test new source behaviour
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_Source = Sources('CNN', 'Russian ukraine war to keep on going','www.cnn.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_Source, Sources))
        
        
# if __name__ =='__main__':
#     unittest.main()
    