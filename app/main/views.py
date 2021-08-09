from flask import render_template
from flask import current_app


# views
@main.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''
    title = "Home - The World On Your Lap"
    all_news = get_news('sports')
    general_news = get_news('general')
    tech_news = get_news('technology')
    bus_news = get_news('business')
    ent_news = get_news('entertainment')

    # print(all_news)

    return render_template('index.html', title=title, sports=all_news, general=general_news, technology=tech_news,
                           business=bus_news, entertainment=ent_news)
