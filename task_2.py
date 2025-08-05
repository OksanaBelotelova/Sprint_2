class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        super().add_movie(movie)
        return print(f'Комедии: {self.movies}')


class Drama(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self, movie):
        super().add_movie(movie)
        return print(f'Драмы: {self.movies}')


comedy = Comedy()
comedy.add_movie('Большой куш')
drama = Drama()
drama.add_movie('Оружейный барон')
