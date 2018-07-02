class Song(object):
    def __init__(self, lyrics, singer):
        self.lyrics = lyrics
        self.singer = singer
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    def sing_my_song(self):
        print(self.singer)

happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"
], "Maron")

bull_on_parade = Song([
    "They rally around tha family",
    "With pockets full of shells"
], "Hela")

happy_bday.sing_me_a_song()
happy_bday.sing_my_song()


print("Sing a ling")
bull_on_parade.sing_me_a_song()
bull_on_parade.sing_my_song()

