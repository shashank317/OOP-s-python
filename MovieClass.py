class Movie:
    def __init__(self, movie_name, rating):
        self.movie_name = movie_name
        self.rating = rating

    def display(self):
        print(f"Movie Name: {self.movie_name}")
        print(f"Rating: {self.rating}")


movie1 = Movie("war",4.5)

movie1.display()
