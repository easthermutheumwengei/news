class News:
    '''
    News class to define news objects
    '''

    def __init__(self, name, url, description, country, category, id):
        self.name = name
        self.url = url
        self.description = description
        self.country = country
        self.category = category
        self.id = id