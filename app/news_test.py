import unittest
from app.models import news
News = news.News

class NewsTest(unittest.TestCase):
        '''
        Test class to test the behavior of the news source class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_source = News('Al Jazeera English', 'http://www.aljazeera.com', 'News, analysis from the Middle East and worldwide', 'usa',
                                        'general', 'al-jazeera-english')

        def test_instance(self):
            '''
            '''
            self.assertTrue(isinstance(self.new_source, News))

        def test_to_check_instance_variables(self):
            '''
            '''
            self.assertEquals(self.new_source.name, 'Al Jazeera English')
            self.assertEquals(self.new_source.url, 'http://www.aljazeera.com')
            self.assertEquals(self.new_source.description, 'News, analysis from the Middle East and worldwide')
            self.assertEquals(self.new_source.country, 'usa')
            self.assertEquals(self.new_source.category, 'general')
            self.assertEquals(self.new_source.id, 'al-jazeera-english')


if __name__ == '__main__':
    unittest.main()