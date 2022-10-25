# https://docs.python.org/3/reference/datamodel.html
class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @property
    def likes(self):
        return self._likes

    @name.setter
    def name(self, name):
        self._name = name.title()

    def give_likes(self):
        self._likes += 1

    def __str__(self):
        return f'{self._name} - {self.year} - {self.likes} likes'


class Film(Program):

    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self._name} - {self.year} - {self.duration} min - {self.likes} likes'


class Serie(Program):

    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season

    def __str__(self):
        return f'{self._name} - {self.year} - {self.season} seasons - {self.likes} likes'

class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    def __len__(self):
        return len(self._programs)

    @property
    def listing(self):
        return self._programs

    @property
    def size_playlist(self):
        return len(self._programs)


avengers = Film('Avengers Infinity war', 2018, 160)
atlanta = Serie('Atlanta', 2016, 2)
encanto = Film('Encanto',2021, 102)
swat = Serie('S.W.A.T.',2017, 6)

avengers.give_likes()
avengers.give_likes()
avengers.give_likes()
encanto.give_likes()
encanto.give_likes()
encanto.give_likes()
encanto.give_likes()
atlanta.give_likes()
atlanta.give_likes()
swat.give_likes()
swat.give_likes()

films_series = [avengers, swat, encanto, atlanta]
weekend_playlist = Playlist('Weekend List', films_series)

print(f'Size of playlist: {len(weekend_playlist)}')

for program in weekend_playlist:
    print(program)

