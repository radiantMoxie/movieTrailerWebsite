import media
import fresh_tomatoes


# All the instances of the Movie class
bridget_joness_diary = media.Movie("Bridget Jones's Diary",
                                   "A singleton takes on London",
                                   "BridgetJonesDiaryMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=DQdy98B1nf0",
                                   "R",
                                   "Renee Zellweger, Hugh Grant, Colin Firth",
                                   "2001")

sliding_doors = media.Movie("Sliding Doors",
                            "A woman's life takes a very different path when she makes the train",
                            "Slidingdoors.jpg",
                            "https://www.youtube.com/watch?v=4u7akRLnGyk",
                            "PG-13",
                            "Gwyneth Paltrow, John Hannah",
                            "1998")

sex_and_the_city = media.Movie("Sex and the City",
                               "Four friends take on love and relationships in NYC",
                               "Sex_and_the_City_The_Movie.jpg",
                               "https://www.youtube.com/watch?v=y6U8o9Ed0VI",
                               "R",
                               "Sarah Jessica Parker, Kim Cattrall, Kristin Davis, \
                                Cynthia Nixon",
                               "2008")

# the array that holds all the Movie objects
movies = [bridget_joness_diary, sliding_doors, sex_and_the_city]                                 

fresh_tomatoes.open_movies_page(movies)

