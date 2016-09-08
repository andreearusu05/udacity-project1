import webbrowser

class Movie():
    """
    Create a class containing properties of movies
    
    Attributes:
        movie_title (str): Name of the movie
        poster_image (str): The poster image 
        trailer_youtube (str): The youtube trailer
    """
    
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
