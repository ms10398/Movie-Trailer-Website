import webbrowser
class Movie():
    """ class contains all the required information about the movies"""
    #function containes all the required information about the movie
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title #inputs movies title
        self.storyline = movie_storyline #inputs movies storyline
        self.poster_image_url   = poster_image #inputs movies poster image
        self.trailer_youtube_url = trailer_youtube #inputs movies youtube trailer


    #function used to play the trailer using youtube url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
