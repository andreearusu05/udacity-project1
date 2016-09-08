import media
import fresh_tomatoes

# Create an object of type Movie called brooklyn
brooklyn = media.Movie("Brooklyn",
                       "http://cdn3-www.comingsoon.net/assets/uploads/4840/09/file_610952_brooklyn-poster-640x951.jpg",
                       "https://www.youtube.com/watch?v=15syDwC000k")

# Create an object of type Movie called csl (stands for Crazy Stupid Love)
csl = media.Movie("Crazy Stupid Love",
                  "http://cdn.collider.com/wp-content/uploads/crazy-stupid-love-movie-poster-5.jpg",
                  "https://www.youtube.com/watch?v=8iCwtxJejik")

# Create an object of type Movie called notebook
notebook = media.Movie("The Notebook",
                       "http://www.impawards.com/2004/posters/notebook_ver4_xlg.jpg",
                       "https://www.youtube.com/watch?v=S3G3fILPQAU")

# Create a list of the aforementioned movies
movies = [brooklyn, csl, notebook]

# Open the movies page
fresh_tomatoes.open_movies_page(movies)
