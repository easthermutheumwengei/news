import unittest
from app.models import Articles


class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''

    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles('Title', 'Title description', 'https://google.com/images',
                                    '2018-05-12T13:31:03Z', 'nimo', 'buzzfeed.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.title, 'Title')
        self.assertEquals(self.new_article.description, 'Title description')
        self.assertEquals(self.new_article.image, 'https://google.com/images')
        self.assertEquals(self.new_article.publishedAt, '2018-05-12T13:31:03Z')
        self.assertEquals(self.new_article.author, 'nimo')
        self.assertEquals(self.new_article.url, 'buzzfeed.com')

if __name__ == '__main__':
    unittest.main()