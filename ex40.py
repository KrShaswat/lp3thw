class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song (["Happy Birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song (["They rally around tha family",
                         "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Study Drill 1
munni = Song (["Munni Badnaam hui Darling Tere Liye",
                "Munni nayan sharabi, hoth gulabi",
                "Wo jhandu baam hui Darling tere liye"])

danda = Song (["Kaal se pehle wahi tha",
                "Kaal ke baad wahi hai",
                "Na jaane kitne Barso se le raha wo teri",
                "Teri Teri Teri Teri"])

print("")
munni.sing_me_a_song()
danda.sing_me_a_song()

# Study Drill 2
black_sheep = ["Baa Baa Black Sheep",
                "Have you any wool",
                "yes sir yes sir",
                "Three bags full"]

poem = Song(black_sheep)
poem.sing_me_a_song()
