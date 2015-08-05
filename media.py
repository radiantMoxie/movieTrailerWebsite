import webbrowser

class Movie():

    """This class creates a Movie object.\n
    It's populated with movie basics and the ability to play the trailer."""


    # class variable of ratings
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # The class constructor
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, rating, starring, release_year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        self.starring = starring
        self.release_year = release_year
        

    # method that plays the film's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
